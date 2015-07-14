FROM    python:2.7

MAINTAINER Santiago del Castillo

ADD app /app

WORKDIR /app

RUN pip install -r requirements.txt

# Expose port
EXPOSE  5000

CMD ["python", "app.py"]
