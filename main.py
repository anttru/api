from cryptoApi.controller import CryptoValueController
from cryptoApi.models import CrytoValueModel
from cryptoApi.view import CryptoValueView

class App:
    def __init__(self) -> None:
        self.model = CrytoValueModel()
        self.view = CryptoValueView(self.model)
        self.controller = CryptoValueController(self.model, self.view)


if __name__ == "__main__":
    app = App()
    app.controller.execute()
