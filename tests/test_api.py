from fastapi.testclient import TestClient

import sys 
sys.path.append(r".")
from src.main import create_application  


# client testing
app = create_application()
test_client = TestClient(app)


def test_add_user( test_client: TestClient = test_client):
    user_data = {
        "id": "test_user",
        "nom": "John Doe",
        "age" : 33 , 
        "prenom" : "idris"
    }
    
    response = test_client.post("/api/add_users", json=user_data)
    assert response.status_code == 201
    assert response.json()["user_id"] == "test_user"


def test_update_user(test_client: TestClient= test_client):
    
    user_id = "test_user"
    updated_data = {
        "id": "test_user",
        "nom": "modified",
        "age" : 45 , 
        "prenom" : "modified"
    }
    response = test_client.put(f"/api/update_user?user_id={user_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["user_id"] == "test_user"




def test_get_id(test_client: TestClient= test_client):
    user_id = "test_user"  
    response = test_client.get(f"/api/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id