import unittest
from config import app
from routes import UserView
from flask import request



class test_View(unittest.TestCase):    
    c = app.test_client()
    url = "http://127.0.0.1:5000/admin"
    url_source_of_data = "{}/source_of_data/".format(url)
    url_address = "{}/address/".format(url)
    url_customer = "{}/customer/".format(url)
    url_invoice = "{}/invoice/".format(url)
    
    #test if the settings for the userviews are correct
    def test_userview_settings(self):
        uv=UserView
        self.assertEqual(uv.page_size, 5, "page_size = %s instead of 5" % (uv.page_size) ) 

    #test if the routes for the views executes without errors
    def test_viewroutes(self):     
        #Source_of_data
        response = self.c.get(self.url_source_of_data)
        self.assertEqual(response.status_code, 200, "Source_of_data" )
        #Address
        response = self.c.get(self.url_address)
        self.assertEqual(response.status_code, 200, "Address")
        #Customer
        response = self.c.get(self.url_customer)
        self.assertEqual(response.status_code, 200, "Customer")
        #Invoice
        response = self.c.get(self.url_invoice)
        self.assertEqual(response.status_code, 200, "Invoice")

    #test if created Data end up in the database
    def test_create_data(self):

        test2 = self.c.post("/source_of_data/",  data='Date Added')
        #test = self.c.form.get('name')
        print("Hallo {}".format(test2))


#class test_Database(unittest.TestCase):


    #test if created data will be found in the database
    #def test_create_data(self):
     



if __name__ == '__main__':
    unittest.main()
