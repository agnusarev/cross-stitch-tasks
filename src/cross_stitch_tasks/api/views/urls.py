from typing import Any, Tuple, Type

import cross_stitch_tasks.api.views.start as start
import cross_stitch_tasks.api.views.type_of_base_form as type_of_base_form
import cross_stitch_tasks.api.views.type_of_image_form as type_of_image_form


def url(api_instance: Any, api_url: str, name: str) -> Tuple[Type[Any], str, str]:
    return api_instance, api_url, name


urls = [
    url(start.StartApp.as_view("/"), "/", "/"),
    url(type_of_base_form.TypeOfBaseView.as_view("/type/"), "/type/", "type"),
    url(type_of_image_form.TypeOfImageView.as_view("/image/"), "/image/", "image"),
]
