# WordCounter

Wordcounter is a word counter web app written in Python using `Flask` web microframework.

## Installation

In order to install the webapp, use the following command:

    python setup.py install

This should install a command-line tool `wordctr` and then to launch the webapp, run the
following command:

    wordctr launch -p [port]

This will launch the webapp on localhost using given port (if any).

You can also build the app using docker using:

    docker build -t <image_name>:<tag> .

To run the docker container:

    docker run -p 8000:8000 <image_name>