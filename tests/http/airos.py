import unittest
from netengine.backends.http import AirOS

from ..settings import settings


__all__ = ['TestHTTP']


class TestHTTP(unittest.TestCase):

    def setUp(self):
        self.host = settings['base-http']['host']
        self.username = settings['base-http']['username']
        self.password = settings['base-http']['password']
        
        self.device = AirOS(self.host, self.username, self.password)
        self.assertTrue(self.device.__netengine__)
    
    def test_firewall(self):
        self.assertTrue(type(self.device.firewall) == dict)
    
    def test_host_info(self):
        self.assertTrue(type(self.device.host_info) == dict)
    
    def test_airview(self):
        self.assertTrue(type(self.device.airview) == dict)
    
    def test_services(self):
        self.assertTrue(type(self.device.services) == dict)
    
    def test_interfaces(self):
        self.assertTrue(type(self.device.interfaces) == list)
    
    def test_interfaces_properties(self):
        self.assertTrue(type(self.device.interfaces_properties) == dict)
    
    def test_wireless(self):
        self.assertTrue(type(self.device.services) == dict)
    
    def test_wireless_stats(self):
        self.assertTrue(type(self.device.services) == dict)
    
    def test_wireless_polling(self):
        self.assertTrue(type(self.device.polling) == dict)
    
    def test_essid(self):
        self.assertTrue(type(self.device.essid) == str)
    
    def test_frequency(self):
        self.assertTrue(type(self.device.frequency) == str)
        
    def test_rates(self):
        self.assertTrue(type(self.device.rates) == list)
    
    def test_ap_addr(self):
        self.assertTrue(type(self.device.ap_addr) == str)
    
    def test_noisefloor(self):
        self.assertTrue(type(self.device.noisefloor) == int)
    
    def test_mode(self):
        self.assertTrue(type(self.device.mode) == str)