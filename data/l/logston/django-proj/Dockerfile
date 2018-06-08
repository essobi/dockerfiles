FROM python:3.6  
  
RUN apt-get update  
RUN apt-get install -y vim  
  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
RUN groupadd -r user && useradd -r -g user user  
USER user  
  
EXPOSE 9090  
  
CMD ["/usr/local/bin/uwsgi", "--ini", "/app/config.ini"]  
  

