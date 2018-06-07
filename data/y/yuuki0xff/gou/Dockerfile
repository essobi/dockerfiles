FROM golang AS build  
WORKDIR /go/src/github.com/shingetsu-gou/shingetsu-gou  
ADD https://github.com/yuuki0xff/shingetsu-gou/archive/secure.tar.gz
/srv/gou.tar.gz  
RUN tar xvf /srv/gou.tar.gz --strip-components=1  
RUN go get  
  
FROM debian:stable-slim  
EXPOSE 8000  
VOLUME /srv  
WORKDIR /srv  
ENV GOSU_VERSION="1.10" \  
GOU_VERSION="v0.2.8"  
COPY entrypoint /opt/  
COPY config /opt/gou/default_config  
ADD https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-
amd64 /opt/gosu  
COPY \--from=build /go/bin/shingetsu-gou /opt/gou/  
RUN chmod +x /opt/gosu /opt/gou/shingetsu-gou  
CMD ["/opt/entrypoint"]  

