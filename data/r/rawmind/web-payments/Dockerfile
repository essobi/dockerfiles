FROM rawmind/alpine-base:3.6-7  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
  
ENV SERVICE_HOME=/opt/web-payments \  
SERVICE_NAME=web-payments \  
VERSION=0.1 \  
GOMAXPROCS=2 \  
GOROOT=/usr/lib/go \  
GOPATH=/opt/src \  
GOBIN=/gopath/bin  
ENV PATH=$PATH:$SERVICE_HOME  
  
# Add service files  
ADD root /  
  
RUN apk add --update go git musl-dev \  
&& mkdir -p /opt/src ${SERVICE_HOME}; cd /opt/src \  
&& cd /opt/src \  
&& go build -o ${SERVICE_NAME} \  
&& mv ./${SERVICE_NAME} ${SERVICE_HOME}; cd ${SERVICE_HOME} \  
&& chmod +x ${SERVICE_HOME}/${SERVICE_NAME} \  
&& apk del go git musl-dev \  
&& rm -rf /var/cache/apk/* /opt/src  
  
EXPOSE 8080  
WORKDIR ${SERVICE_HOME}  
  
ENTRYPOINT ["/opt/web-payments/web-payments"]  

