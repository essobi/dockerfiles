FROM python:2.7-alpine3.6  
MAINTAINER n0trace,<n0trace@protonmail.com>  
RUN pip install flask gunicorn --no-cache-dir  
WORKDIR /app  
ADD app.py /app/app.py  
EXPOSE 8000  
CMD gunicorn -w 4 -b 0.0.0.0:8000 app:app  

