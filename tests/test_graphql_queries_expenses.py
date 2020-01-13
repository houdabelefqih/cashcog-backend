import pytest


@pytest.mark.django_db
def test_expenses_list(graphql_client, generate_expenses):
    query = ''' {
              expenses {
                edges {
                  node {
                    uuid
                    description
                    amount
                    currency
                    employee {
                      uuid
                      firstName
                      lastName
                    }
                  }
                }
              }
            }

    '''

    result = graphql_client.execute(query)
    assert len(result['data']['expenses']['edges']) == 7





