FROM debian:jessie  
MAINTAINER BeF <bef@eventphone.de>  
WORKDIR /usr/local/src  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y tcl tcllib tcl-tclreadline build-essential zlib1g-dev
libssl-dev libgsm1-dev pkg-config speex libmysqlclient-dev wget  
COPY build_yate.sh ./  
RUN ./build_yate.sh  
  

