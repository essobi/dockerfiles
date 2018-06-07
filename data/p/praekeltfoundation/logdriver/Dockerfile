FROM golang:1.6-onbuild  
MAINTAINER Praekelt Foundation <dev@praekeltfoundation.org>  
  
EXPOSE 3000  
VOLUME /logs  
  
CMD ["go-wrapper", "run", \  
"-directory", "/logs", \  
"-address", "0.0.0.0:3000"]  

