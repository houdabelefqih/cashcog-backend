import pytest


@pytest.mark.django_db
def test_query_employees_with_first_name_filter(graphql_client, generate_employees):
    query = ''' 
                query employees($firstName_Icontains: String!) {
                       employees(firstName_Icontains: $firstName_Icontains) {
                         edges {
                           node {
                             uuid
                             firstName
                             lastName
                           }
                         }
                       }
                     }

        '''

    result = graphql_client.execute(query, variable_values={"firstName_Icontains": "Pau"})

    assert len(result['data']['employees']['edges']) == 2


@pytest.mark.django_db
def test_query_employees_with_last_name_filter(graphql_client, generate_employees):
    query = ''' 
                query employees($lastName_Istartswith: String!) {
                       employees(lastName_Istartswith: $lastName_Istartswith) {
                         edges {
                           node {
                             uuid
                             firstName
                             lastName
                           }
                         }
                       }
                     }

        '''

    result = graphql_client.execute(query, variable_values={"lastName_Istartswith": "V"})

    assert len(result['data']['employees']['edges']) == 3

@pytest.mark.django_db
def test_query_employees_with_last_name_and_first_name_filter(graphql_client, generate_employees):
    query = ''' 
                query employees($lastName_Istartswith: String!, $firstName_Icontains: String!) {
                       employees(lastName_Istartswith: $lastName_Istartswith, firstName_Icontains: $firstName_Icontains) {
                         edges {
                           node {
                             uuid
                             firstName
                             lastName
                           }
                         }
                       }
                     }

        '''

    result = graphql_client.execute(query, variable_values={"lastName_Istartswith": "V", "firstName_Icontains": "min"})

    assert len(result['data']['employees']['edges']) == 1
    assert "min" in result['data']['employees']['edges'][0]['node']['firstName']
    assert result['data']['employees']['edges'][0]['node']['lastName'].startswith('V')
