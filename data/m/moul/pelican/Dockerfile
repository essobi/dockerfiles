FROM ubuntu:trusty  
MAINTAINER Manfred Touron <m@42.am> (@moul)  
  
RUN apt-get -q update && apt-get -y -q upgrade && apt-get -y -q install build-
essential python-pip python-dev git && apt-get clean  
RUN pip install markdown pelican  
RUN mkdir /pelican  
WORKDIR /pelican  
EXPOSE 8000  

