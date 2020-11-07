from students_api import *  # The code to test
import unittest   # The test framework


record_error1 = {
    id: 1,
    name: "Error",
    email: "err@gmailcom",
    gender: None
  }

record_error2 = {
    id: 1,
    email: "err@mailcom",
    gender: None
  }

record_error2 = {
    id: None,
    name: "Error Error Error Error Error Error Error Error Error Error Error Error Error",
    email: "err@mailcom",
    gender: None
  }

record_sucess = {
    id: None,
    name: "sucess",
    email: "sucess@mail.com",
    gender: None
  }


class Test_TestIncrementDecrement(unittest.TestCase):
  def test_isValid1(self):
    self.assertEqual(students_api.record_isvalid(record_error), {"value": False, "column": "email"})

  def test_isValid1(self):
    self.assertEqual(students_api.record_isvalid(record_error), {"value": False, "column": "email"})

if __name__ == '__main__':
  unittest.main()

