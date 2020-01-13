from graphql import GraphQLError

from expenses.schema import ExpenseNode, ExpenseFilter
from .models import Employee
import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {'first_name': ['exact', 'icontains', 'istartswith'],
                  'last_name': ['exact', 'icontains', 'istartswith'],
                  'uuid': ['exact']}


class EmployeeNode(DjangoObjectType):

    expenses = DjangoFilterConnectionField(ExpenseNode, filterset_class=ExpenseFilter)

    class Meta:
        model = Employee
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    employee = graphene.relay.Node.Field(EmployeeNode)
    employees = DjangoFilterConnectionField(EmployeeNode, filterset_class=EmployeeFilter)