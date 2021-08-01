FROM python

RUN pip install pytest pytest-check selenium requests

COPY . /app

WORKDIR /app

CMD [ "bash", "runcase.sh" ]