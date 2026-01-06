from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from firebase_auth import login_user, register_user
from firebase_db import get_stock, update_stock


# ---------- POPUP ----------
def show_popup(title, message):
    popup = Popup(
        title=title,
        content=Label(text=message),
        size_hint=(0.8, 0.4)
    )
    popup.open()


# ---------- LOGIN SCREEN ----------
class LoginScreen(Screen):
    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text

        if not email or not password:
            show_popup("Error", "Please enter email and password")
            return

        res = login_user(email, password)

        if "idToken" in res:
            App.get_running_app().id_token = res["idToken"]
            App.get_running_app().root.current = "inventory"
        else:
            show_popup("Error", res.get("error", {}).get("message", "Login failed"))


# ---------- REGISTER SCREEN ----------
class RegisterScreen(Screen):
    def register(self):
        email = self.ids.email.text
        password = self.ids.password.text

        if not email or not password:
            show_popup("Error", "Please fill all fields")
            return

        res = register_user(email, password)

        if "idToken" in res:
            show_popup("Success", "Registration successful")
            App.get_running_app().root.current = "login"
        else:
            show_popup("Error", res.get("error", {}).get("message", "Registration failed"))


# ---------- INVENTORY SCREEN ----------
class InventoryScreen(Screen):

    def on_enter(self):
        self.refresh_stock("250ml", self.ids.stock_250)
        self.refresh_stock("500ml", self.ids.stock_500)
        self.refresh_stock("1lt", self.ids.stock_1lt)
        self.refresh_stock("2lt", self.ids.stock_2lt)
        self.refresh_stock("20lt", self.ids.stock_20lt)

    def refresh_stock(self, size, label):
        token = App.get_running_app().id_token
        stock = get_stock(size, token)
        label.text = f"Stock: {stock}"

    def modify_stock(self, size, qty_text, label, is_add):
        if not qty_text:
            show_popup("Error", "Enter quantity")
            return

        qty = int(qty_text)
        token = App.get_running_app().id_token
        current = get_stock(size, token)

        if not is_add and qty > current:
            show_popup("Error", "Not enough stock")
            return

        new_value = current + qty if is_add else current - qty
        update_stock(size, new_value, token)
        label.text = f"Stock: {new_value}"


# ---------- MAIN APP ----------
class InventoryApp(App):
    id_token = ""

    def build(self):
        Builder.load_file("inventory.kv")

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(InventoryScreen(name="inventory"))

        return sm

    def logout(self):
        self.id_token = ""
        self.root.current = "login"


if __name__ == "__main__":
    InventoryApp().run()
