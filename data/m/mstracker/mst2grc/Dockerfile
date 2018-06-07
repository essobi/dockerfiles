FROM python:alpine  
  
WORKDIR /src  
ADD . .  
  
RUN pip install --upgrade pip setuptools && \  
pip install -r requirements.txt && \  
pip install gunicorn json-logging-py  
  
COPY gunicorn/gunicorn.conf /  
COPY gunicorn/logging.conf /  
  
ENV GUNICORN_BIND 0.0.0.0:5000  
ENV GUNICORN_WORKERS 1  
EXPOSE 5000  
CMD ["gunicorn", "wsgi:app", "--config", "/gunicorn.conf", "--log-config",
"/logging.conf", "--access-logfile=-"]  

