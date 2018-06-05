FROM gliderlabs/consul  
MAINTAINER Jose-Luis Rivas <me@ghostbar.co>  
  
ENV GOPATH /opt/go  
RUN apk --update add go git && \  
mkdir -p /opt/go && \  
go get github.com/AcalephStorage/consul-alerts && \  
apk del git go && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 9000  
CMD []  
ENTRYPOINT [ "/opt/go/bin/consul-alerts" ]  

