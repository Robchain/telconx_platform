import unittest
import json
from app import app

class TestTelcoXAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        """Test del endpoint de salud"""
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('timestamp', data)

    def test_get_customer_consumption_valid_id(self):
        """Test para obtener consumo de cliente válido"""
        response = self.app.get('/api/customer/12345/consumption')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['customer_id'], '12345')
        self.assertEqual(data['customer_name'], 'Juan Pérez')
        self.assertIn('data', data)
        self.assertIn('minutes', data)
        self.assertIn('balance', data)

    def test_get_customer_consumption_invalid_id(self):
        """Test para obtener consumo de cliente inválido"""
        response = self.app.get('/api/customer/99999/consumption')
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Customer not found')

    def test_get_customers_list(self):
        """Test para obtener lista de clientes"""
        response = self.app.get('/api/customers')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)
        
        # Verificar estructura del primer cliente
        customer = data[0]
        self.assertIn('id', customer)
        self.assertIn('name', customer)
        self.assertIn('plan', customer)

    def test_consumption_data_structure(self):
        """Test para verificar estructura de datos de consumo"""
        response = self.app.get('/api/customer/12345/consumption')
        data = json.loads(response.data)
        
        # Verificar campos obligatorios
        required_fields = ['customer_id', 'customer_name', 'plan', 'balance', 'data', 'minutes', 'last_updated']
        for field in required_fields:
            self.assertIn(field, data)
        
        # Verificar estructura de datos
        data_fields = ['consumed_gb', 'limit_gb', 'remaining_gb', 'usage_percentage']
        for field in data_fields:
            self.assertIn(field, data['data'])
        
        # Verificar estructura de minutos
        minutes_fields = ['consumed', 'limit', 'remaining', 'usage_percentage']
        for field in minutes_fields:
            self.assertIn(field, data['minutes'])

if __name__ == '__main__':
    unittest.main()