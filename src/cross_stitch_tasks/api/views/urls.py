from typing import Any, Tuple, Type

import cross_stitch_tasks.api.views.start as start


def url(api_instance: Any, api_url: str, name: str) -> Tuple[Type[Any], str, str]:
    return api_instance, api_url, name


urls = [
    url(start.StartApp.as_view("/"), "/", "/"),
]
