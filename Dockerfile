FROM python:latest

RUN pip install flask
COPY hello.py /tmp/hello.py

EXPOSE 5000
CMD ["python","/tmp/hello.py"]

