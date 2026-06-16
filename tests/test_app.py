import unittest
from app import app

class AppTest(unittest.TestCase):

    def setUp(self):
        # Creates a test client to simulate requests
        self.client = app.test_client()

    def test_home_route(self):
        # ✅ Passing test: checks if "/" returns 200 and contains text
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("CI/CD Demo Application", response.data.decode())

    def test_fail_route(self):
        # ❌ Failing test: expects 200 but /fail raises an error
        response = self.client.get("/fail")
        self.assertEqual(response.status_code, 200)  # This will fail

if __name__ == "__main__":
    unittest.main()
