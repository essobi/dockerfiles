FROM ubuntu:12.04  
MAINTAINER Matt Ward  
  
RUN apt-get update  
RUN apt-get -y install software-properties-common python-software-properties  
RUN add-apt-repository ppa:fkrull/deadsnakes  
RUN apt-get update  
RUN apt-get -y install python2.7 python-pip  
  
CMD ["python"]  

