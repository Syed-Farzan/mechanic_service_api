from rest_framework import status
from rest_framework.test import APITestCase

from .models import Mechanic


class MechanicAPITest(APITestCase):
    def setUp(self):
        self.mechanic = Mechanic.objects.create(
            name="Ali Motors",
            phone="9876543210",
            location="Jammu",
            rating="4.50",
            is_open=True,
            services=[
                "Oil Change",
                "Engine Repair",
                "Brake Repair",
            ],
        )

    def test_create_mechanic(self):
        data = {
            "name": "Khan Garage",
            "phone": "9876543211",
            "location": "Srinagar",
            "rating": "4.20",
            "is_open": True,
            "services": [
                "Oil Change",
                "Tire Repair",
            ],
        }

        response = self.client.post(
            "/api/mechanics/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["name"], "Khan Garage")

    def test_invalid_mechanic_phone(self):
        data = {
            "name": "Bad Garage",
            "phone": "123",
            "location": "Jammu",
            "rating": "4.50",
            "is_open": True,
            "services": [
                "Oil Change",
            ],
        }

        response = self.client.post(
            "/api/mechanics/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("phone", response.data)


class ServiceRequestAPITest(APITestCase):
    def setUp(self):
        self.mechanic = Mechanic.objects.create(
            name="Ali Motors",
            phone="9876543210",
            location="Jammu",
            rating="4.50",
            is_open=True,
            services=[
                "Oil Change",
                "Engine Repair",
                "Brake Repair",
            ],
        )

    def test_create_service_request(self):
        data = {
            "customer_name": "Arhan",
            "customer_phone": "9876543212",
            "vehicle_number": "JK01AB1234",
            "mechanic": self.mechanic.id,
            "service": "Oil Change",
            "problem_description": "The engine oil needs to be changed.",
        }

        response = self.client.post(
            "/api/service-requests/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["status"], "PENDING")

        self.assertEqual(response.data["mechanic"], self.mechanic.id)

    def test_service_not_provided_by_mechanic(self):
        data = {
            "customer_name": "Arhan",
            "customer_phone": "9876543212",
            "vehicle_number": "JK01AB1234",
            "mechanic": self.mechanic.id,
            "service": "Battery Service",
            "problem_description": "Battery issue.",
        }

        response = self.client.post(
            "/api/service-requests/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("service", response.data)

    def test_non_existent_mechanic(self):
        data = {
            "customer_name": "Arhan",
            "customer_phone": "9876543212",
            "vehicle_number": "JK01AB1234",
            "mechanic": 9999,
            "service": "Oil Change",
            "problem_description": "Oil change needed.",
        }

        response = self.client.post(
            "/api/service-requests/",
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("mechanic", response.data)
