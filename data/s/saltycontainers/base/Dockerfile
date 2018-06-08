FROM resin/amd64-debian:jessie  
  
MAINTAINER Bruno Binet <bruno.binet@gmail.com>  
  
RUN apt-get update && apt-get install -y make  
  
WORKDIR /root/saltycontainers  
COPY Makefile minion ./  
RUN make deps thin  
  
COPY states ./states/  
COPY reclass ./reclass/  
RUN make apply_formula  
RUN make apply_build  
  
ENV INITSYSTEM on  

