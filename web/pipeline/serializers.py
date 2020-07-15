from rest_framework import serializers

from .models import Location, Community, CensusSubdivision, LocationDistance


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", "community_id", "location_type", "latitude", "longitude", "location_fuzzy")


class CommunitySerializer(serializers.ModelSerializer):

    wildfire_zone = serializers.SlugRelatedField(read_only=True, slug_field='risk_class')
    tsunami_zone = serializers.SlugRelatedField(read_only=True, slug_field='zone_class')

    class Meta:
        model = Community
        fields = (
            "id",
            "place_name",
            "latitude",
            "longitude",
            "census_subdivision",
            "community_type",
            'base_access_50mbps',
            'fn_community_name',
            'municipality_classification',
            'estimated_population',
            'estimated_total_dwellings',
            "wildfire_zone",
            "tsunami_zone",
            "num_schools",
            "num_courts",
            "num_hospitals",
            "num_timber_facilities",
        )


class CensusSubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusSubdivision
        exclude = ['geom', 'geom_simplified']


class LocationDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDistance
        fields = (
            "id",
            "community",
            "location",
            "distance",
            # "travel_time",
            # "travel_time_display", "driving_route_available"
        )
