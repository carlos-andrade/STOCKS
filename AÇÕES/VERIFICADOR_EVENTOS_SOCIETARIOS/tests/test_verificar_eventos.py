import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verificar_eventos.py"
SPEC = importlib.util.spec_from_file_location("verificar_eventos", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class CorporateActionVerifierTests(unittest.TestCase):
    def test_reverse_split_factor_must_be_below_one(self):
        event = {
            "event_id": "TEST-RS-1", "ticker": "TEST3", "event_type": "GRUPAMENTO",
            "new_shares_per_old_share": 0.1, "effective_date": "2020-01-01",
            "source_url": "https://ri.example.com/event", "source_type": "RI_EMISSOR",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertEqual(MODULE.validate_verified_event(event), [])

    def test_split_factor_must_be_above_one(self):
        event = {
            "event_id": "TEST-S-1", "ticker": "TEST3", "event_type": "DESDOBRAMENTO",
            "new_shares_per_old_share": 5, "effective_date": "2020-01-01",
            "source_url": "https://ri.example.com/event", "source_type": "RI_EMISSOR",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertEqual(MODULE.validate_verified_event(event), [])

    def test_search_candidate_cannot_be_accepted_as_verified_without_review(self):
        event = {
            "event_id": "TEST-S-2", "ticker": "TEST3", "event_type": "DESDOBRAMENTO",
            "new_shares_per_old_share": 2, "effective_date": "2020-01-01",
            "source_url": "https://example.com/search-snippet", "source_type": "OUTRA_FONTE",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertTrue(MODULE.validate_verified_event(event))

    def test_zero_factor_is_invalid(self):
        event = {
            "event_id": "TEST-RS-2", "ticker": "TEST3", "event_type": "GRUPAMENTO",
            "new_shares_per_old_share": 0, "effective_date": "2020-01-01",
            "source_url": "https://ri.example.com/event", "source_type": "RI_EMISSOR",
            "verification_status": "VERIFICADO", "verified_by": "reviewer",
            "verified_at": "2020-01-01T00:00:00Z"
        }
        self.assertTrue(MODULE.validate_verified_event(event))


if __name__ == "__main__":
    unittest.main()
