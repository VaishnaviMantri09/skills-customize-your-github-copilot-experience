import unittest
import importlib.util
import pathlib

# Load starter-code.py as a module regardless of folder name
HERE = pathlib.Path(__file__).resolve().parent
MODULE_PATH = HERE.parent / "starter-code.py"
spec = importlib.util.spec_from_file_location("starter_code", str(MODULE_PATH))
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)


class TestSearchSort(unittest.TestCase):
    def test_linear_and_binary_search_found(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(sc.linear_search(arr, 5), 2)
        self.assertEqual(sc.binary_search(arr, 5), 2)

    def test_search_not_found(self):
        arr = [2, 4, 6, 8]
        self.assertEqual(sc.linear_search(arr, 3), -1)
        self.assertEqual(sc.binary_search(arr, 3), -1)

    def test_sorts(self):
        arr = [5, 2, 9, 1, 5]
        self.assertEqual(sc.bubble_sort(arr), sorted(arr))
        self.assertEqual(sc.merge_sort(arr), sorted(arr))


if __name__ == "__main__":
    unittest.main()
