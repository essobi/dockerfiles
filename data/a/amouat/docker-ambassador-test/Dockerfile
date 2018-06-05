FROM alpine:latest  
  
MAINTAINER Adrian Mouat adrian@adrianmouat.com  
  
RUN apk --update add socat  
CMD env | grep _TCP= | \  
sed 's/.*_PORT_\\([0-9]*\\)_TCP=tcp:\/\/\\(.*\\):\\(.*\\)/socat
TCP4-LISTEN:\1,fork,reuseaddr TCP4:\2:\3 \&/' \  
| sh && top  
  

