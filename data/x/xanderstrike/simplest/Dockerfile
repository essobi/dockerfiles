FROM ubuntu:latest  
MAINTAINER Alex Standke "xanderstrike@gmail.com"  
VOLUME ["/data"]  
RUN apt-get update -y  
RUN apt-get install -y python-pip python-dev build-essential  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python"]  
CMD ["server.py"]  

