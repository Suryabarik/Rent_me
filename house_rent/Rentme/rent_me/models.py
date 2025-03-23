from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, null=False)
    mobile_number = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.full_name

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('PG', 'PG'),
        ('Room', 'Room'),
    ]

    property_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, null=False)
    location = models.CharField(max_length=255, null=False)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    availability = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.property_type} at {self.location}"

class PGDetails(models.Model):
    pg_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    pg_name = models.CharField(max_length=100, null=False)
    room_type = models.CharField(max_length=50, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    meal_type = models.CharField(max_length=50, blank=True, null=True)
    preferred_tenants = models.CharField(max_length=50, blank=True, null=True)
    features = models.CharField(max_length=50, blank=True, null=True)
    additional_details = models.CharField(max_length=50, blank=True, null=True)
    image1 = models.CharField(max_length=256, blank=True, null=True)
    image2 = models.CharField(max_length=256, blank=True, null=True)
    image3 = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.pg_name

class RoomDetails(models.Model):
    room_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    room_title = models.CharField(max_length=100, null=False)
    room_size = models.CharField(max_length=50, blank=True, null=True)
    floor_number = models.IntegerField(blank=True, null=True)
    bathroom_type = models.CharField(max_length=50, blank=True, null=True)
    preferred_tenants = models.CharField(max_length=50, blank=True, null=True)
    features = models.CharField(max_length=50, blank=True, null=True)
    additional_details = models.CharField(max_length=50, blank=True, null=True)
    image1 = models.CharField(max_length=256, blank=True, null=True)
    image2 = models.CharField(max_length=256, blank=True, null=True)
    image3 = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.room_title
