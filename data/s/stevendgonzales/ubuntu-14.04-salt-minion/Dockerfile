FROM stackbrew/ubuntu:trusty  
MAINTAINER Steven Gonzales <stevendgonzales@gmail.com>  
  
RUN apt-get update -q && \  
apt-get install -q -y python-software-properties software-properties-common  
RUN add-apt-repository ppa:saltstack/salt  
RUN apt-get update -q && apt-get install -q -y salt-minion  
  
CMD salt-minion -l debug  

