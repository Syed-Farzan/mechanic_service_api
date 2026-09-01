from rest_framework import serializers

from .models import Mechanic, ServiceRequest

VALID_SERVICES = [
    "Oil Change",
    "Engine Repair",
    "Brake Repair",
    "Tire Repair",
    "Battery Service",
]


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = "__all__"

    def validate_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return value

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError("Rating must be between 0 and 5.")

        return value

    def validate_services(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Services must be provided as a list.")

        if not value:
            raise serializers.ValidationError("At least one service is required.")

        invalid_services = [
            service for service in value if service not in VALID_SERVICES
        ]

        if invalid_services:
            raise serializers.ValidationError(
                f"Invalid services: {', '.join(invalid_services)}"
            )

        return value


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = "__all__"
        read_only_fields = ["id", "status", "created_at"]

    def validate_customer_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return value

    def validate_vehicle_number(self, value):
        value = value.strip().upper()

        if len(value) < 6:
            raise serializers.ValidationError("Invalid vehicle number.")

        return value

    def validate(self, attrs):
        mechanic = attrs.get("mechanic")
        service = attrs.get("service")

        if mechanic and service:
            if service not in mechanic.services:
                raise serializers.ValidationError(
                    {
                        "service": (
                            "This mechanic does not provide " "the selected service."
                        )
                    }
                )

        return attrs
