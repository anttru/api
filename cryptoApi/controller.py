from cryptoApi.models import CrytoValueModel
from cryptoApi.view import CryptoValueView

class CryptoValueController:
    def __init__(self):
        self.view = CryptoValueView()
            
    def execute(self):
        self.view.mainloop()
        
    

    