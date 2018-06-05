FROM ubuntu:15.10  
  
MAINTAINER scott.miller171@gmail.com  
  
RUN apt-get update  
RUN apt-get dist-upgrade -yq  
RUN apt-get install python python-dev python-pip libyaml-dev -yq  
RUN pip install ansible  
RUN apt-get clean  
RUN rm -Rf ~/.pip/cache/  

