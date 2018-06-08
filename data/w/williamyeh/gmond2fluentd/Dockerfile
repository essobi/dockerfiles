# Docker image for gmond2fluentd  
#  
# pull base image  
FROM williamyeh/dash  
#FROM williamyeh/busybox-sh  
#FROM busybox  
#FROM progrium/busybox  
#FROM alpine:3.1  
#FROM debian:jessie  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
  
WORKDIR /opt  
COPY gmond2fluentd_static_linux-amd64 /opt/gmond2fluentd  
COPY wrapper /opt/  
  
ENTRYPOINT ["/opt/wrapper"]  
CMD ["--help"]

