FROM golang:alpine  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apk --update add git protobuf geoip  
RUN go get github.com/AcalephStorage/kviator  
RUN go get github.com/golang/protobuf/protoc-gen-go  
RUN go get -d github.com/tonnerre/geocolo/geocolo-service  
RUN cd /go/src/github.com/tonnerre/geocolo; protoc --go_out=plugins=grpc:.
*.proto  
RUN cd /go/src/github.com/tonnerre/geocolo/geocolo-service; go install  
  
RUN ["/usr/sbin/addgroup", "-S", "_geocolo"]  
RUN ["/usr/sbin/adduser", "-S", "-h", "/nonexistent", "-H", "-g", "Geolocation
Service user", "-g", "_geocolo", "-D", "_geocolo"]  
  
RUN ["/usr/bin/install", "-o", "_geocolo", "-g", "_geocolo", "-m", "0755",
"-d", "/etc/geocolo"]  
RUN ["/usr/bin/install", "-o", "root", "-g", "root", "-m", "0700", "-d",
"/run/geocolo-certs"]  
  
RUN ["/etc/periodic/monthly/geoip"]  
  
ADD config-and-run-geocolo.sh /usr/bin/config-and-run-geocolo.sh  
  
RUN ["/bin/chmod", "0555", "/usr/bin/config-and-run-geocolo.sh"]  
  
EXPOSE 1234/tcp  
VOLUME ["/etc/geocolo", "/run/geocolo-certs"]  
USER _geocolo  
  
CMD ["/bin/sh", "/usr/bin/config-and-run-geocolo.sh"]  

