FROM ubuntu:latest  
MAINTAINER Dominik Sachsenhofer "dominik@sachsenhofer.io"  
RUN apt-get update  
RUN apt-get install -y python-pip python-dev build-essential wget curl  
COPY . /app  
WORKDIR /app  
  
RUN pip install -r requirements.txt  
  
EXPOSE 5000  
ENTRYPOINT ["python"]  
  
CMD ["app.py"]  

