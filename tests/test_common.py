from typing import Any, TYPE_CHECKING

from tests.base_test import BaseTest


class TestCommon(BaseTest):

    def test_app(self, crud: Any) -> None:
        if TYPE_CHECKING:
            print(crud)
        assert True
