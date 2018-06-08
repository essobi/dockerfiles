FROM golang:1.10-alpine  
  
# Install docker  
RUN apk update --no-cache && \  
apk add docker git bash  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT [ "/entrypoint.sh" ]  

