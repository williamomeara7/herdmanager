from django.urls import path
from .views import (
    AssetHolderList,
    AnimalList,
    AnimalGradeList,
    ValuePointList,
    AnimalResourceList,
)

urlpatterns = [
    path("asset_holders/", AssetHolderList.as_view(), name="asset_holder-list"),
    path("animals/", AnimalList.as_view(), name="animal-list"),
    path("animal_grades/", AnimalGradeList.as_view(), name="animal_grade-list"),
    path("value_points/", ValuePointList.as_view(), name="value_point-list"),
    path(
        "animal_resources/", AnimalResourceList.as_view(), name="animal_resource-list"
    ),
]
