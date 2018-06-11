FROM ubuntu:16.04  
MAINTAINER Tyghe Vallard "vallardt@gmail.com"  
RUN apt-get update -y  
RUN apt-get install -y python-pip python-dev libmagickwand-dev  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python"]  
CMD ["app.py"]  

