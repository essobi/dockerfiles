FROM golang:alpine  
MAINTAINER Rushairer <rushairer@163.com>  
  
RUN apk --no-cache add make bash  
  
COPY ./resources/github.com /go/src/github.com  
  
WORKDIR /go/src/github.com/flike/kingshard  
RUN source ./dev.sh \  
&& make \  
&& ln -s /go/src/github.com/flike/kingshard/bin/kingshard
/usr/local/bin/kingshard  
  
VOLUME ["/etc/ks.yaml"]  
EXPOSE 9696 9797  
COPY ./resources/docker-kingshard-entrypoint /usr/local/bin  
CMD ["docker-kingshard-entrypoint"]  
  

