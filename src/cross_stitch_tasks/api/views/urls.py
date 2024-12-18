from typing import Any, Tuple, Type

import cross_stitch_tasks.api.views.start as start
import cross_stitch_tasks.api.views.type_of_base_form as type_of_base_form
import cross_stitch_tasks.api.views.type_of_image_form as type_of_image_form
import cross_stitch_tasks.api.views.jobs_form as jobs_form
import cross_stitch_tasks.api.views.processes_form as processes_form
import cross_stitch_tasks.api.views.delete_object as delete_object


def url(api_instance: Any, api_url: str, name: str) -> Tuple[Type[Any], str, str]:
    return api_instance, api_url, name


urls = [
    url(start.StartApp.as_view("/index/"), "/", "index"),
    url(type_of_base_form.TypeOfBaseView.as_view("/type/"), "/type/", "type"),
    url(type_of_base_form.TypeOfBase.as_view("/types_list/"), "/types_list/", "types_list"),
    url(type_of_image_form.TypeOfImageView.as_view("/image/"), "/image/", "image"),
    url(type_of_image_form.TypeOfImage.as_view("/images_list/"), "/images_list/", "images_list"),
    url(jobs_form.JobView.as_view("/job/"), "/job/", "job"),
    url(jobs_form.Job.as_view("/job_list/"), "/job_list/", "job_list"),
    url(processes_form.ProcessesView.as_view("/processes/<int:id>/"), "/processes/<int:id>/", "processes"),
    url(delete_object.DeleteJobsView.as_view("/delete/<int:id>/"), "/delete/<int:id>/", "delete"),
]
