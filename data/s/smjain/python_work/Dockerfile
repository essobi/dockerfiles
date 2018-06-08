FROM ubuntu:12.04  
MAINTAINER Matt Ward  
COPY . /app1  
WORKDIR /app1  
RUN apt-get update  
RUN apt-get -y install software-properties-common python-software-properties  
RUN add-apt-repository ppa:fkrull/deadsnakes  
RUN apt-get update  
RUN apt-get -y install python2.7 python-pip  
RUN pip install kafka-python  
ENTRYPOINT ["python"]  
CMD ["app.py"]  

