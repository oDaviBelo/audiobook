from audio import app
from mykey import mypass
if __name__ == "__main__":
    app.run(debug=True)
app.secret_key = mypass
