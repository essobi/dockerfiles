FROM ubuntu:12.04  
COPY . /src  
  
#ENV DEBIAN_FRONTEND noninteractive  
RUN cd /src && apt-get update && apt-get install -y python-pip && pip install
-r requirements.txt  
  
EXPOSE 8000  
CMD cd /src && python wsgi.py  

