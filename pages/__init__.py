from .app import App
from .login import Login
from .home import Home

# pages for the application for ease of use
pages = {
    "Login": Login,
    "Home": Home,
}

app = App(pages)
app.mainloop()
