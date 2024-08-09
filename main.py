from audio import app
from mykey import mypass
from config import config

app.config.from_object(config)


if __name__ == "__main__":
    app.run(debug=True)
app.secret_key = mypass
