from pyexpat import model
from cryptoApi.models import CrytoValueModel
from cryptoApi import COINS
import tkinter as tk
from tkinter import ttk

class CryptoValueView:
    
    def __init__(self, model : CrytoValueModel):
        self.origin = "BTC"
        self.destination = "EUR"
        self.petitionFlag = 0
        self.model = model

        self.window = tk.Tk()
        self.labelTop= tk.Label(self.window, text = "ExchangePro")
        self.labelTop.grid(column = 0, row = 0)
        self.labelFrom = tk.Label(self.window, text = "Convert from: ")
        self.labelFrom.grid(column = 0, row = 1)
        self.labelFrom = tk.Label(self.window, text = "to: ")
        self.labelFrom.grid(column = 0, row = 2)
        
        self.fromAmount = tk.StringVar(value = 1)
        self.entryFrom = tk.Entry(self.window, textvariable = self.fromAmount)
        self.entryFrom.grid(column = 3, row = 1)
        
        self.toAmount = tk.StringVar()
        self.entryTo = tk.Entry(self.window, textvariable = self.toAmount)
        self.entryTo["state"] = "readonly"
        self.entryTo.grid(row = 2, column = 3)

        self.selectedOrigin = tk.StringVar()
        self.selectFrom = ttk.Combobox(self.window, values = COINS, textvariable= self.selectedOrigin)
        self.selectFrom.grid(column = 1, row = 1)
        self.selectFrom.current(2)
        self.selectFrom["state"] = "readonly"
        self.selectFrom.bind("<<ComboboxSelected>>", self.setOrigin)

        self.selectedDestination = tk.StringVar()
        self.selectTo = ttk.Combobox(self.window, values = COINS, textvariable= self.selectedDestination)
        self.selectTo.grid(column = 1, row = 2)
        self.selectTo.current(0)
        self.selectTo["state"] = "readonly"
        self.selectTo.bind("<<ComboboxSelected>>", self.setDestination)

        self.button = tk.Button(self.window, text = "Convert", command = self.informAndAskModel)
        self.button.grid(row = 2, column = 4)

    def informAndAskModel(self):
        self.model.origin = self.origin
        self.model.destination = self.destination
        self.model.getRate()
        self.toAmount.set(self.model.calculate(self.fromAmount.get()))
        
    def setOrigin(self, event):
        self.origin = self.selectedOrigin.get()

    def setDestination(self, event):
        self.destination = self.selectedDestination.get()
    
    def mainloop(self):
        self.window.mainloop()

