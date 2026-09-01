from django.db import models


class Mechanic(models.Model):
    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    location = models.CharField(max_length=255)

    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    is_open = models.BooleanField(default=True)

    services = models.JSONField(default=list)

    def __str__(self):
        return self.name


class ServiceRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACCEPTED = "ACCEPTED", "Accepted"
        COMPLETED = "COMPLETED", "Completed"

    customer_name = models.CharField(max_length=100)

    customer_phone = models.CharField(max_length=15)

    vehicle_number = models.CharField(max_length=30)

    mechanic = models.ForeignKey(
        Mechanic, on_delete=models.CASCADE, related_name="service_requests"
    )

    service = models.CharField(max_length=100)

    problem_description = models.TextField()

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle_number}"
