import pandas as pd

from cross_stitch_tasks.api.data_base_helper import DataBaseHelper
from tests.base_test import BaseTest


class TestDataBaseHelper(BaseTest):

    def test_insert_types_of_base(self, crud: "DataBaseHelper") -> None:
        expected = pd.DataFrame.from_dict({"id": [1, 2], "type_of_base": ["пластик", "дерево"]})
        crud.insert("types_of_base", {"type_of_base": "пластик"})
        crud.insert("types_of_base", {"type_of_base": "дерево"})
        test_df = crud.get_actual_table("types_of_base")

        pd.testing.assert_frame_equal(expected, test_df)

    def test_insert_types_of_image(self, crud: "DataBaseHelper") -> None:
        expected = pd.DataFrame.from_dict({"id": [1, 2], "type_of_image": ["пейзаж", "цветы"]})
        crud.insert("types_of_image", {"type_of_image": "пейзаж"})
        crud.insert("types_of_image", {"type_of_image": "цветы"})
        test_df = crud.get_actual_table("types_of_image")

        pd.testing.assert_frame_equal(expected, test_df)
