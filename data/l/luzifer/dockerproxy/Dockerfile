FROM golang  
  
MAINTAINER Knut Ahlers <knut@ahlers.me>  
  
RUN go get github.com/Luzifer/dockerproxy && \  
go install github.com/Luzifer/dockerproxy && \  
mkdir /etc/dockerproxy  
  
VOLUME ["/etc/dockerproxy"]  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["/go/bin/dockerproxy", "-configfile=/etc/dockerproxy/config.json"]  

