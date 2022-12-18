from . import create_app

app = create_app()


@app.route("/")
def index():
    app.logger.warning("hello world")
    return "Hello World!"
