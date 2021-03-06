import unittest
from .models import news
import Business
Business=business.Business

class  BusinessTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_business=Business('null','The Guardian','Julia Kollewe','Irn-Bru maker raises prices as UK inflation soars','https://i.guim.co.uk/img/media/0adcb8d724386e3f524b399ad6b9028ac65fd283/0_116_3500_2100/master/3500.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=12dd7ec2853f62fba3ff23b070b3bbed','G Barr blames rising production costs for price increase as it ups full-year sales and profit estimatesThe company behind Irn-Bru has revealed it is increasing its prices after its packaging, ingredients and energy-linked commodity costs jumped, as it raised','https://amp.theguardian.com/business/2022/feb/01/irn-bru-raises-prices-uk-inflation-ag-barr-sales-profit','2022-02-01T08:55:30Z','The company behind Irn-Bru has revealed it is increasing its prices after its packaging, ingredients and energy-linked commodity costs jumped, as it raised its sales and profit estimates.\r\nAG Barr sa… [+1933 chars]')
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_business=Business))


    def tearDown(self):
        self.news_sources = None
    

    def test_init_id(self):
        self.assertEqual(self.news_business.id, "null")

    def test_init_name(self):
        self.assertEqual(self.news_business.name, "The Guardian")

    def test_init_author(self):
      
        self.assertEqual(self.news_business.author, "Julia Kollewe")

    def test_init_title(self):
        self.assertEqual(self.news_business.title, "Irn-Bru maker raises prices as UK inflation soars")

    def test_init_Image(self):
     
        self.assertEqual(self.news_business.Image, "https://i.guim.co.uk/img/media/0adcb8d724386e3f524b399ad6b9028ac65fd283/0_116_3500_2100/master/3500.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=12dd7ec2853f62fba3ff23b070b3bbed",)

    def test_init_description(self):
     
        self.assertEqual(self.news_business.description, "AG Barr blames rising production costs for price increase as it ups full-year sales and profit estimatesThe company behind Irn-Bru has revealed it is increasing its prices after its packaging, ingredients and energy-linked commodity costs jumped, as it raised…")
    def test_init_url(self):
     
        self.assertEqual(self.news_business.url, "https://amp.theguardian.com/business/2022/feb/01/irn-bru-raises-prices-uk-inflation-ag-barr-sales-profit")

    def test_init_time(self):
        
        self.assertEqual(self.news_business.time, "2022-02-01T08:55:30Z")
     
     def test_init_content(self):
     
        self.assertEqual(self.news_business.content, "The company behind Irn-Bru has revealed it is increasing its prices after its packaging, ingredients and energy-linked commodity costs jumped, as it raised its sales and profit estimates.\r\nAG Barr sa… [+1933 chars]")


if __name__ == "__main__":
    unittest.main()