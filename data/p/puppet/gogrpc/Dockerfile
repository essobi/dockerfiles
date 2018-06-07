FROM golang:latest as builder  
RUN apt update && apt install unzip  
COPY ./buildit.sh /tmp  
WORKDIR /go  
  
RUN cd /tmp && ./buildit.sh && rm ./buildit.sh  

