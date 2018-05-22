FROM python:3

ADD . /wordcounter

WORKDIR /wordcounter

RUN pip install -r requirements.txt

RUN python setup.py install

CMD [ "python", "wordcounter/app.py", "launch" ]