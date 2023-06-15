FROM python:3

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY *.py /app/
COPY templates /app/
RUN chmod a+x *.py

CMD ["/app.py"]



