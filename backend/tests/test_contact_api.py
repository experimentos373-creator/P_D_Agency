"""Tests for P&D Agency contact API endpoint"""
import pytest
import requests
import os

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')


class TestContactAPI:
    """Contact form submission endpoint tests"""

    def test_root_health(self):
        response = requests.get(f"{BASE_URL}/api/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data

    def test_submit_contact_success(self):
        payload = {
            "name": "TEST_João Silva",
            "email": "test@example.com",
            "package_interest": "Pacote Projeto",
            "message": "Gostaria de saber mais sobre os vossos serviços."
        }
        response = requests.post(f"{BASE_URL}/api/contact", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data.get("success") is True
        assert "message" in data

    def test_submit_contact_without_package(self):
        payload = {
            "name": "TEST_Maria Santos",
            "email": "maria@test.com",
            "message": "Mensagem de teste sem pacote."
        }
        response = requests.post(f"{BASE_URL}/api/contact", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data.get("success") is True

    def test_submit_contact_missing_required_fields(self):
        payload = {"name": "TEST_Missing"}
        response = requests.post(f"{BASE_URL}/api/contact", json=payload)
        assert response.status_code == 422  # Validation error

    def test_get_contacts(self):
        response = requests.get(f"{BASE_URL}/api/contact")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_data_persisted_after_submit(self):
        payload = {
            "name": "TEST_Persistence Check",
            "email": "persist@test.com",
            "package_interest": "Manutenção",
            "message": "Verificação de persistência."
        }
        requests.post(f"{BASE_URL}/api/contact", json=payload)
        # Verify in list
        get_response = requests.get(f"{BASE_URL}/api/contact")
        assert get_response.status_code == 200
        submissions = get_response.json()
        names = [s.get("name") for s in submissions]
        assert "TEST_Persistence Check" in names
