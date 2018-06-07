FROM ubuntu  
MAINTAINER James Gregory <james@jagregory.com>  
  
# install pngcrush  
RUN echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main
universe" > /etc/apt/sources.list  
RUN apt-get update -y && apt-get install -y pngcrush  
  
RUN mkdir -p /source  
WORKDIR /source  
  
ENTRYPOINT ["pngcrush"]  

