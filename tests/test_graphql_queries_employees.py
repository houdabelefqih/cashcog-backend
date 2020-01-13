import pytest
import uuid


@pytest.mark.django_db
def test_employees_list(graphql_client, generate_employees):

    query = ''' {

        employees{
          edges{
            node{
              uuid
              firstName
              lastName
            }
          }
        }
        
      }

    '''

    result = graphql_client.execute(query)
    assert len(result['data']['employees']['edges']) == 7


@pytest.mark.django_db
def test_query_specific_employee_with_invalid_field(graphql_client, employee):

    query = ''' 
               query employees($uuid: UUID!) {
                      employees(uuid: $uuid) {
                        edges {
                          node {
                            uuid
                            firstName
                            address
                          }
                        }
                      }
                    }

       '''

    result = graphql_client.execute(query, variable_values={"uuid": str(employee.uuid)})
    assert "errors" in result
    assert "Cannot query field" in result['errors'][0]['message']


@pytest.mark.django_db
def test_query_specific_employee_with_valid_fields(graphql_client, employee):

    query = ''' 
               query employees($uuid: UUID!) {
                      employees(uuid: $uuid) {
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

    result = graphql_client.execute(query, variable_values={"uuid": str(employee.uuid)})

    assert result == {
              "data": {
                "employees": {
                  "edges": [
                    {
                      "node": {
                        "uuid": str(employee.uuid),
                        "firstName": employee.first_name,
                        "lastName": employee.last_name
                      }
                    }
                  ]
                }
              }
            }


@pytest.mark.django_db
def test_query_specific_employee_with_invalid_uuid(graphql_client, employee):

    query = ''' 
               query employees($uuid: UUID!) {
                      employees(uuid: $uuid) {
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

    result = graphql_client.execute(query, variable_values={"uuid": "435afc4b-f345-43e2-ad3d-b59cb6bb05f"})
    assert "errors" in result
    assert result['errors'][0]['message'] == "badly formed hexadecimal UUID string"


@pytest.mark.django_db
def test_query_specific_employee_with_nonexistent_uuid(graphql_client, employee):

    query = ''' 
               query employees($uuid: UUID!) {
                      employees(uuid: $uuid) {
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

    result = graphql_client.execute(query, variable_values={"uuid": str(uuid.uuid4())})
    assert not result['data']['employees']['edges']


