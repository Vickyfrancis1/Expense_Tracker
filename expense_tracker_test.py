import unittest

def category_totals(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] = totals[category] + expense["amount"]
        else:
             totals[category] = expense["amount"]
    return totals

class TestTotals(unittest.TestCase):
    
    def test_groups_by_category(self):
        data = [
            {"description": "Bread", "amount": 500, "category": "Food"},
            {"description": "Taxi", "amount": 1500, "category": "Transport"},
            {"description": "Rice", "amount": 3000, "category": "Food"},
        ]
        self.assertEqual(category_totals(data), {"Food": 3500, "Transport": 1500})
         
    def test_empty(self):
        self.assertEqual(category_totals([]), {})
         
unittest.main(exit=False)