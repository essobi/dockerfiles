FROM ubuntu:vivid  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y install git  
  
COPY . /  
VOLUME ["/input", "/output", "/cache", "/ssh"]  
CMD ["/scripts/run.sh"]  

