import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError

from .models import Expense
from employees.schema import EmployeeNode, EmployeeFilter


class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = {'uuid': ['exact'],
                  'description': ['iexact', 'icontains'],
                  'created_at': ['exact', 'date', 'year', 'month', 'day', 'time', 'hour'],
                  'amount': ['exact', 'gt', 'gte', 'lt','lte'],
                  'currency': ['iexact', 'icontains'],
                  'approved': ['iexact'],

                  }
        interfaces = [graphene.relay.Node, ]


class ExpenseNode(DjangoObjectType):
    class Meta:
        model = Expense
        interfaces = [graphene.relay.Node, ]


class Query(graphene.ObjectType):
    expense = graphene.relay.Node.Field(ExpenseNode)
    expenses = DjangoFilterConnectionField(ExpenseNode, filterset_class=ExpenseFilter)


class ExpenseMutation(graphene.Mutation):
    uuid = graphene.UUID()
    description = graphene.String()
    created_at = graphene.DateTime()
    amount = graphene.Decimal()
    currency = graphene.String()
    employee = graphene.Field(EmployeeNode)
    approved = graphene.Boolean()

    class Arguments:
        uuid = graphene.UUID()
        approved = graphene.Boolean()

    def mutate(self, info, uuid, approved):

        try:
            expense = Expense.objects.get(pk=uuid)

        except Expense.DoesNotExist:
            raise GraphQLError("This uuid does not exist.")

        expense.approved = approved
        expense.save()

        return ExpenseMutation(uuid=expense.uuid,
                               description=expense.description,
                               created_at=expense.created_at,
                               amount=expense.amount,
                               currency=expense.currency,
                               employee=expense.employee,
                               approved=expense.approved)


class Mutation(graphene.ObjectType):
    update_expense = ExpenseMutation.Field()
