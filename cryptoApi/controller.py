from cryptoApi import view
from cryptoApi.models import CrytoValueModel
from cryptoApi.view import CryptoValueView

class CryptoValueController:
    def __init__(self, model : CrytoValueModel, view : CryptoValueView):
        self.model = model
        self.view = view
            
    def execute(self):
        self.view.mainloop()
        
    

    