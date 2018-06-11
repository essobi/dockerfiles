FROM alpine:edge  
MAINTAINER Dominique DERRIER derrierdo@gmail.com  
RUN apk add --update python3  
RUN pip3 install docker-py  
ADD html /www  
ENTRYPOINT /www/server.py  
#EXPOSE 8000:8000  
#ENTRYPOINT /Start.sh  

