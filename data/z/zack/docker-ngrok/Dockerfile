FROM golang:1.4.1-cross  
  
MAINTAINER YuLun Shih <shih@yulun.me>  
  
VOLUME ["/data"]  
  
ENV GOPATH /data/gopath  
  
ADD ./scripts /scripts  
  
ENTRYPOINT ["/scripts/app.sh"]  
  
CMD ["start"]

