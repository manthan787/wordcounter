import click
from flask import Flask, render_template, request
from counter import Wordcounter
from errors import EMPTY_INPUT_ERROR

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("index.html", word_count=0, text="")

    if request.method == 'POST':
        text = request.form.get('text')
        error = ""
        if not text:
            error = EMPTY_INPUT_ERROR
        counter = Wordcounter(text)
        return render_template("index.html",
                               word_count=counter.count(),
                               text=text, error=error)


@app.route("/wordcounter", methods=['POST'])
def word_count():
    data = request.form.get('text')
    if not data:
        return str(0)
    return str(Wordcounter(data).count())


@click.group()
def main():
    pass


@main.command()
@click.option("--port", "-p", type=click.INT, default=8000,
              help="Port on which to run the web application")
def launch(port):
    app.run(port=port)


if __name__ == "__main__":
    main()
