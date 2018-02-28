__author__ = 'Pavan Kotehal'


from rest_framework import serializers
from .models import Student, User, branches_college, YEAR_IN_SCHOOL_CHOICES


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fname = serializers.CharField(max_length=50)
    lname = serializers.CharField(required=False, max_length=50)
    age = serializers.IntegerField()
    branches = serializers.ChoiceField(choices=branches_college, default='ELECTRONICS_COMMUNICATIONS')
    year_in_school = serializers.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES, default='FRESHMAN')

    def create(self, validated_data):
        """
        Create and return a new `Student` instance, given the validated data.
        :param validated_data:
        :return:
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Student` instance, given the validated data
        :param instance:
        :param validated_data:
        :return:
        """
        instance.fname = validated_data('fname', instance.fname)
        instance.lname = validated_data('lname', instance.lname)
        instance.age = validated_data('age', instance.age)
        instance.branches = validated_data('branches', instance.branches)
        instance.year_in_school = validated_data('year_in_school', instance.year_in_school)
        instance.save()
        return instance