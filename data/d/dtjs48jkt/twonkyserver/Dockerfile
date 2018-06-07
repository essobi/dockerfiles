FROM phusion/baseimage:0.9.22  
  
# Set correct environment variables  
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" LC_ALL="C.UTF-8"
LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
ADD setup.sh /tmp/  
RUN bash /tmp/setup.sh  
  
VOLUME /config  
VOLUME /data  
  
EXPOSE 1030/udp 1900/udp 9000/tcp  

