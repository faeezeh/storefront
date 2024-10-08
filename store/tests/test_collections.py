from django.contrib.auth.models import User
from store.models import Collection
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
import pytest

@pytest.fixture
def create_collection(api_client):
    def d0_create_collection(collection):
        # Return the response from the post request
        return api_client.post('/store/collections/', collection)
    return d0_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    # skip test
    # @pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self,create_collection):
        #AAA (Arrange, Act, Assert)
        response = create_collection({'title':'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self,authenticate,create_collection):
   
        authenticate()
        response = create_collection({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_invalid_returns_400(self,authenticate,create_collection):
   
        authenticate()
        response = create_collection({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None   
    
    def test_if_user_is_valid_returns_201(self,authenticate,create_collection):
   
        authenticate()
        response = create_collection({'title':'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0    

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self, api_client):
        # Arrange
        collection = baker.make(Collection)
        print(collection.__dict__)  # Optional: useful for debugging if needed
        
        # Act: Retrieve the collection using the API
        response = api_client.get(f'/store/collections/{collection.id}/')

        # Assert: Check if the response status code is 200
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title':collection.title,
            'products_count': 0
        }
