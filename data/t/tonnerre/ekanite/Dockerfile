FROM golang:alpine  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apk --update add git  
RUN go get github.com/ekanite/ekanite  
RUN go install github.com/ekanite/ekanite/cmd/ekanited  
  
RUN ["/usr/sbin/addgroup", "-S", "_ekanited"]  
RUN ["/usr/sbin/adduser", "-S", "-h", "/nonexistent", "-H", "-g", "Ekanite
syslog server", "-g", "_ekanited", "-D", "_ekanited"]  
  
RUN ["/usr/bin/install", "-o", "_ekanited", "-g", "_ekanited", "-m", "0700",
"-d", "/srv/ekanited"]  
  
USER _ekanited:_ekanited  
EXPOSE 5514/tcp 5514/udp 8080/tcp 9950/tcp 9951/tcp  
VOLUME ["/srv/ekanited"]  
ENTRYPOINT ["/go/bin/ekanited"]  
CMD ["-datadir", "/srv/ekanited", "-diag", "0.0.0.0:9951", "-query",
"0.0.0.0:9950", "-queryhttp", "0.0.0.0:8080", "-tcp", "0.0.0.0:5514", "-udp",
"0.0.0.0:5514"]  

