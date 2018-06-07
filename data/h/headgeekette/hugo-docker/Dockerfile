FROM golang:latest  
MAINTAINER Charo Nuguid <me@thegeekettespeaketh.com>  
  
RUN apt-get update  
  
RUN go get -u -v github.com/spf13/hugo  
  
EXPOSE 1313  
WORKDIR /source  
  
ENTRYPOINT ["hugo"]  
  
CMD ["help"]  

