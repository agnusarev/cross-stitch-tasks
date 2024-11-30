from typing import Any

from tests.base_test import BaseTest


class TestCommon(BaseTest):

    def test_insert(self, crud: Any) -> None:
        crud.insert("types_of_base", {"type_of_base": "лен"})
        crud.insert("types_of_base", {"type_of_base": "дерево"})

        assert crud.get_actual_table("types_of_base").shape[1] == 2
