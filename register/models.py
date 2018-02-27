from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    ELECTRONICS_COMMUNICATIONS = 'EC'
    COMPUTER_SCIENCE = 'CS'
    INFORMATION_SCIENCE = 'IS'
    MECHANICAL = 'ME'
    INSTRUMENTATION = 'IT'
    branches_college = (
        (ELECTRONICS_COMMUNICATIONS, 'Electronics & Communication'),
        (COMPUTER_SCIENCE, 'Computer Science'),
        (INFORMATION_SCIENCE, 'Informatin Science'),
        (MECHANICAL, 'Mechanical'),
        (INSTRUMENTATION, 'Instrumentation'),
    )

    branches = models.CharField(
        max_length=2,
        choices=branches_college,
        default=ELECTRONICS_COMMUNICATIONS
    )

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'

    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def __str__(self):
        return "{0} {1}".format(self.fname, self.lname)

    def is_upperclass(self):
        return self.year_in_school(self.JUNIOR, self.SENIOR)
