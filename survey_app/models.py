# from django.db import models


# from django.contrib.auth.models import AbstractUser
# from django.db import models

# from django.contrib.auth.models import AbstractUser
# from django.db import models


# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)  # Ensure email is unique

#     groups = models.ManyToManyField(
#         Group,
#         related_name="customuser_set",  # Unique related_name to avoid conflicts
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name="customuser_permissions_set",  # Unique related_name to avoid conflicts
#         blank=True
#     )

#     def __str__(self):
#         return self.username  # String representation of the user


# # class CustomUser(AbstractUser):
# #     groups = models.ManyToManyField(
# #         "auth.Group",
# #         related_name="customuser_set",  # <-- Unique related_name
# #         blank=True
# #     )
# #     user_permissions = models.ManyToManyField(
# #         "auth.Permission",
# #         related_name="customuser_permissions_set",  # <-- Unique related_name
# #         blank=True
# #     )





# # class CustomUser(AbstractUser):
# #     email = models.EmailField(unique=True)
# #     is_admin = models.BooleanField(default=False)

# #     def _str_(self):
# #         return self.username

# class Survey(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     # tea = models.DecimalField(max_digits=6, decimal_places=2)
#     # coffee = models.DecimalField(max_digits=6, decimal_places=2)
#     # biscuit = models.DecimalField(max_digits=6, decimal_places=2)
#     # smoking = models.DecimalField(max_digits=6, decimal_places=2)

#     tea = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#     coffee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#     biscuit = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#     smoking = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)




#     submitted_at = models.DateTimeField(auto_now_add=True)
#     is_approved = models.BooleanField(default=False)
#     @property
#     def daily_expenses(self):
#         return self.tea + self.coffee + self.biscuit + self.smoking
#     @property
#     def weekly_expenses(self):
#         return self.daily_expenses * 7  # Assuming 7 days in a week

#     @property
#     def monthly_expenses(self):
#         return self.daily_expenses * 30  # Assuming 30 days in a month




from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One user can have only one survey
    tea = models.PositiveIntegerField(default=0)      # Number of tea cups per day
    coffee = models.PositiveIntegerField(default=0)   # Number of coffee cups per day
    biscuit = models.PositiveIntegerField(default=0)  # Number of biscuit packets per day
    smoking = models.PositiveIntegerField(default=0)  # Number of cigarettes per day
    is_approved = models.BooleanField(default=False)  # Admin approval status

    def __str__(self):
        return f"{self.user.username}'s Survey"

    # Calculate total monthly expenses
    def total_monthly_expense(self):
        daily_expense = self.tea + self.coffee + self.biscuit + self.smoking
        return daily_expense * 30  # Assuming 30 days in a month

    # Calculate weekly expenses
    def total_weekly_expense(self):
        return self.total_monthly_expense() / 4  # Approximate weekly expenses

    # Calculate daily expenses
    def total_daily_expense(self):
        return self.total_monthly_expense() / 30  # Average daily expenses
