import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError

from .models import Expense


class ExpenseFilter(django_filters.FilterSet):

    class Meta:
        model = Expense
        fields = {'uuid': ['exact'],
                  'description': ['iexact', 'icontains'],
                  'created_at': ['date', 'week_day','year', 'month', 'day', 'time', 'hour'],
                  'amount': ['exact', 'gt', 'gte', 'lt', 'lte'],
                  'currency': ['iexact', 'icontains'],
                  'status': ['iexact'],
                  }

        interfaces = [graphene.relay.Node, ]


class ExpenseNode(DjangoObjectType):
    class Meta:
        model = Expense
        interfaces = [graphene.relay.Node, ]


class Query(graphene.ObjectType):
    expense = graphene.relay.Node.Field(ExpenseNode)
    expenses = DjangoFilterConnectionField(ExpenseNode, filterset_class=ExpenseFilter)


class ExpenseMutation(graphene.relay.ClientIDMutation):
    class Input:
        uuid = graphene.UUID(required=True)
        status = graphene.String(required=True)

    expense = graphene.Field(ExpenseNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):

        uuid = input.get('uuid')

        try:
            expense = Expense.objects.get(pk=uuid)

        except Expense.DoesNotExist:
            raise GraphQLError("This uuid does not exist.")

        expense.status = input.get('status')
        expense.save()

        return ExpenseMutation(expense=expense)


class Mutation(graphene.AbstractType):
    update_expense = ExpenseMutation.Field()
