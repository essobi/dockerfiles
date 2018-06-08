# Docker image for minimal Ganglia Monitoring Daemon  
#  
  
  
# pull base image  
FROM williamyeh/dash  
#FROM williamyeh/busybox-sh  
#FROM busybox  
#FROM progrium/busybox  
#FROM alpine:3.1  
#FROM debian:jessie  
  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
  
ADD rootfs.tar.gz /  
  
#USER ganglia  
  
# gmond ports  
EXPOSE 8649  
  
VOLUME ["/etc/ganglia/conf.d"]  
  
  
# for convenience  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY gmond.conf /etc/ganglia/  
  
  
# Define default command.  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["gmond"]  
#CMD ["gmond", "--debug", "2"]  
#CMD ["gmond", "--conf", "/etc/ganglia/gmond.conf"]  
#CMD ["gmetric", "-t", "float", "-n", "test_process", "-v", "200", "-u",
"Bytes"]  

