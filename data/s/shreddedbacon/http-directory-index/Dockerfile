FROM alpine:latest  
  
RUN apk update  
RUN apk upgrade  
RUN apk add --no-cache bash git curl wget jq coreutils  
  
COPY scripts/ /opt/resource/  
RUN chmod +x /opt/resource/*  
  
RUN apk del git  

