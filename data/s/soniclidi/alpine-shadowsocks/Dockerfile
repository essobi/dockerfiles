FROM alpine:latest  
  
MAINTAINER soniclidi  
  
RUN apk update && apk add py-pip  
RUN pip install shadowsocks  
  
ENTRYPOINT ["/usr/bin/ssserver"]  

