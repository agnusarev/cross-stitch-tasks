import pandas as pd
from flask import Flask
from sqlalchemy import select

from cross_stitch_tasks.api.data_base_helper import DataBaseHelper
from cross_stitch_tasks.api.models import TypeOfBase, TypeOfImage
from tests.base_test import BaseTest


class TestDataBaseHelper(BaseTest):

    def test_insert(self, crud: "DataBaseHelper") -> None:
        type_of_base_dict = {"type_of_base": "пластик"}
        crud.insert("types_of_base", type_of_base_dict)
        _type_of_base = crud.db.session.execute(select(TypeOfBase.type_of_base)).scalar_one()
        assert _type_of_base == type_of_base_dict["type_of_base"]

        type_of_image_dict = {"type_of_image": "пейзаж"}
        crud.insert("types_of_image", type_of_image_dict)
        _type_of_image = crud.db.session.execute(select(TypeOfImage.type_of_image)).scalar_one()
        assert _type_of_image == type_of_image_dict["type_of_image"]

    def test_get_actual_table(self, crud: "DataBaseHelper") -> None:
        expected = pd.DataFrame.from_dict({"id": [1], "type_of_image": ["пейзаж"]})
        test_df = crud.get_actual_table("types_of_image")

        pd.testing.assert_frame_equal(expected, test_df)


class TestApi(BaseTest):
    def test_forms(self, get_client_: "Flask") -> None:
        response = get_client_.get("/type")
        assert response.status_code == 200  # type: ignore

        response = get_client_.get("/image")
        assert response.status_code == 200  # type: ignore
