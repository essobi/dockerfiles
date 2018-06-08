FROM python:3  
MAINTAINER Neel Bedekar "neel.bedekar@gmail.com"  
ENV APP_SETTINGS=production  
ENV FLASK_APP=/app/run.py  
COPY . /app  
COPY gunicorn_config.py /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
CMD ["gunicorn", "--config", "/app/gunicorn_config.py", "run:app"]

