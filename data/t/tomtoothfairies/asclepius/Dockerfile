FROM python:3.6-alpine  
MAINTAINER Eoin Houlihan <ehoulih@tcd.ie>  
  
# Set exposed ports  
EXPOSE 5000  
ENV PYTHONPATH=asclepius  
ENV FLASK_CONFIGURATION=production  
  
RUN apk --no-cache add gcc musl-dev  
  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
  
# Cache python deps  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
CMD ["gunicorn", "-w", "9", "-b", ":5000", "-k", "eventlet", "--log-config",
"asclepius/gunicorn_logging.conf", "main:app"]  

