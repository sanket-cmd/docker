FROM Python

WORKDIR/.app

COPY ./app

RUN pip install -r requirment.txt

ENTRYPOINT ["Python3","s3tos3.py"]