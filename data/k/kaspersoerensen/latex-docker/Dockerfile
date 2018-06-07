FROM blang/latex  
MAINTAINER Kasper Soerensen <kasper@kaspersoerensen.dk>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q  
RUN apt-get install -qy curl  
  
WORKDIR /latex  
VOLUME [“/latex”]

