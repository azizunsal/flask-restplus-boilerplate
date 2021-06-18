FROM python:3.8.0
WORKDIR /flask-proj
ADD requirements.txt /flask-proj
RUN python --version
RUN pip --version
RUN pip install -r requirements.txt

ADD . /flask-proj

ENV FLASK_ENV=prod

ENTRYPOINT ["make","run"]
