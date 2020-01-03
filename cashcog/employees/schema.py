from .models import Employee
import graphene
from graphene_django import DjangoObjectType


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class Query(graphene.AbstractType):
    employees = graphene.List(EmployeeType)

    def resolve_employees(self, info):
        return Employee.objects.all()

