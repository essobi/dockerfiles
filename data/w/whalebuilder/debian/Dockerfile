FROM debian:stretch  
MAINTAINER Hubert Chathi <hubert@uhoreg.ca>  
  
RUN groupadd -r whalebuilder && useradd -r -g whalebuilder -d
/home/whalebuilder -m whalebuilder  
WORKDIR /home/whalebuilder  
  
RUN apt-get update && apt-get install -y build-essential  

