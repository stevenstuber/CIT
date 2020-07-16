from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

import pipeline.views


urlpatterns = [
    url(r"^auth/$", pipeline.views.auth),
    url(r"^locations/geojson/$", pipeline.views.LocationGeoJSONList.as_view()),
    url(r"^locations/$", pipeline.views.LocationList.as_view()),
    url(r"^communities/geojson/$", pipeline.views.CommunityGeoJSONList.as_view()),
    url(r"^communities/(?P<pk>[0-9]+)/$", pipeline.views.CommunityDetail.as_view()),
    url(r"^communities/$", pipeline.views.CommunityList.as_view()),
    url(r"^censussubdivisions/geojson/$", pipeline.views.CensusSubdivisionGeoJSONList.as_view()),
    url(r"^censussubdivisions/(?P<pk>[0-9]+)/$", pipeline.views.CensusSubdivisionDetail.as_view()),
    url(r"^censussubdivisions/$", pipeline.views.CensusSubdivisionList.as_view()),
    # TODO: add distances
    url(r"^locationdistances/geojson/$", pipeline.views.LocationDistanceGeoJSONList.as_view()),
    url(r"^locationdistances/$", pipeline.views.LocationDistanceList.as_view()),
    path('openapi', get_schema_view(title="CIT", description="API for CIT", version="1.0.0"), name='openapi-schema'),
    path(
        'api/',
        TemplateView.as_view(template_name='swagger-ui.html', extra_context={'schema_url': 'openapi-schema'}),
        name='swagger-ui',
    ),
]
