FROM python:2.7  
MAINTAINER lfries@cozero.com.au  
  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
EXPOSE 2368  
CMD ["uwsgi", "wsgi.ini"]

