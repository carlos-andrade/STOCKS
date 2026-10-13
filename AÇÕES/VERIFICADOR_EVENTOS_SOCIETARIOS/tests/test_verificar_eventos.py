import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verificar_eventos.py"
SPEC = importlib.util.spec_from_file_location("verificar_eventos", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class CorporateActionVerifierTests(unittest.TestCase):
    def test_all_registered_verified_events_are_consistent(self):
        events, errors = MODULE.load_events()
        self.assertEqual(errors, [])
        self.assertGreaterEqual(len(events), 3)
        for event in events:
            if event.get("verification_status") == "VERIFICADO":
                self.assertEqual(MODULE.validate_verified_event(event), [], event.get("event_id"))

    def test_pending_candidate_is_reported_as_warn_not_verified(self):
        event = {
            "event_id": "TEST-CANDIDATE-2000", "ticker": "TEST3", "event_type": "DESDOBRAMENTO",
            "post_event_shares_per_pre_event_share": 10, "effective_date": "2000-06-22",
            "source_url": "https://example.com/secondary", "source_type": "OUTRA_FONTE",
            "verification_status": "PENDENTE", "verified_by": None, "verified_at": None,
            "notes": "Candidato secundário; não usar em cálculos."
        }
        status, report = MODULE.build_report("TEST3", [event], [], [], [], True)
        self.assertEqual(status, "WARN")
        self.assertIn("Estado de verificação: PENDENTE", report)
        self.assertIn("Fator total (ações após / ações antes): 10", report)
        self.assertNotIn("Estado de verificação: VERIFICADO", report)
    def test_reverse_split_factor_must_be_below_one(self):
        event = {
            "event_id": "TEST-RS-1", "ticker": "TEST3", "event_type": "GRUPAMENTO",
            "post_event_shares_per_pre_event_share": 0.1, "effective_date": "2020-01-01",
            "source_url": "https://ri.example.com/event", "source_type": "RI_EMISSOR",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertEqual(MODULE.validate_verified_event(event), [])

    def test_split_factor_must_be_above_one(self):
        event = {
            "event_id": "TEST-S-1", "ticker": "TEST3", "event_type": "DESDOBRAMENTO",
            "post_event_shares_per_pre_event_share": 5, "effective_date": "2020-01-01",
            "source_url": "https://ri.example.com/event", "source_type": "RI_EMISSOR",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertEqual(MODULE.validate_verified_event(event), [])

    def test_bonus_factor_must_be_above_one(self):
        event = {
            "event_id": "TEST-BONUS-1", "ticker": "TEST3", "event_type": "BONIFICACAO",
            "post_event_shares_per_pre_event_share": 4 / 3, "effective_date": "2020-01-01",
            "source_url": "https://ri.example.com/event", "source_type": "RI_EMISSOR",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertEqual(MODULE.validate_verified_event(event), [])

    def test_bonus_factor_of_one_is_invalid(self):
        event = {
            "event_id": "TEST-BONUS-2", "ticker": "TEST3", "event_type": "BONIFICACAO",
            "post_event_shares_per_pre_event_share": 1, "effective_date": "2020-01-01",
            "source_url": "https://ri.example.com/event", "source_type": "RI_EMISSOR",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertTrue(MODULE.validate_verified_event(event))

    def test_search_candidate_cannot_be_accepted_as_verified_without_review(self):
        event = {
            "event_id": "TEST-S-2", "ticker": "TEST3", "event_type": "DESDOBRAMENTO",
            "post_event_shares_per_pre_event_share": 2, "effective_date": "2020-01-01",
            "source_url": "https://example.com/search-snippet", "source_type": "OUTRA_FONTE",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertTrue(MODULE.validate_verified_event(event))

    def test_zero_factor_is_invalid(self):
        event = {
            "event_id": "TEST-RS-2", "ticker": "TEST3", "event_type": "GRUPAMENTO",
            "post_event_shares_per_pre_event_share": 0, "effective_date": "2020-01-01",
            "source_url": "https://ri.example.com/event", "source_type": "RI_EMISSOR",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertTrue(MODULE.validate_verified_event(event))


if __name__ == "__main__":
    unittest.main()
