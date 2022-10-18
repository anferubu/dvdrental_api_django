# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        managed = True
        db_table = 'actor'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', models.CASCADE)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    def __str__(self):
        return f'{self.address}, {self.city}'

    class Meta:
        managed = True
        db_table = 'address'
        verbose_name_plural = 'Addresses'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'category'
        verbose_name_plural = 'Categories'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', models.CASCADE)
    last_update = models.DateTimeField()

    def __str__(self):
        return f'{self.city}, {self.country}'

    class Meta:
        managed = True
        db_table = 'city'
        verbose_name_plural = 'Cities'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country

    class Meta:
        managed = True
        db_table = 'country'
        verbose_name_plural = 'Countries'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.SmallIntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, models.CASCADE)
    activebool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        managed = True
        db_table = 'customer'


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language', models.CASCADE)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()
    special_features = models.TextField(blank=True, null=True)
    fulltext = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'film'


class FilmActor(models.Model):
    actor = models.OneToOneField(Actor, models.CASCADE, primary_key=True)
    film = models.ForeignKey(Film, models.CASCADE)
    last_update = models.DateTimeField()

    def __str__(self):
        return f'{self.actor}, {self.film}'

    class Meta:
        managed = True
        db_table = 'film_actor'
        unique_together = (('actor', 'film'),)


class FilmCategory(models.Model):
    film = models.OneToOneField(Film, models.CASCADE, primary_key=True)
    category = models.ForeignKey(Category, models.CASCADE)
    last_update = models.DateTimeField()

    def __str__(self):
        return f'{self.film}, {self.category}'

    class Meta:
        managed = True
        db_table = 'film_category'
        verbose_name_plural = 'Film categories'
        unique_together = (('film', 'category'),)


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.CASCADE)
    store_id = models.SmallIntegerField()
    last_update = models.DateTimeField()

    def __str__(self):
        return self.film.title

    class Meta:
        managed = True
        db_table = 'inventory'
        verbose_name_plural = 'Inventories'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'language'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.CASCADE)
    staff = models.ForeignKey('Staff', models.CASCADE)
    rental = models.ForeignKey('Rental', models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    def __str__(self):
        return f'{self.customer.last_name} (${self.amount})'

    class Meta:
        managed = True
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, models.CASCADE)
    customer = models.ForeignKey(Customer, models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff', models.CASCADE)
    last_update = models.DateTimeField()

    def __str__(self):
        return f'{self.rental_date}, {self.customer.last_name}'

    class Meta:
        managed = True
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, models.CASCADE)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.SmallIntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()
    picture = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        managed = True
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(Staff, models.CASCADE)
    address = models.ForeignKey(Address, models.CASCADE)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.manager_staff.last_name

    class Meta:
        managed = True
        db_table = 'store'
