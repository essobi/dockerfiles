FROM lavenderflowerdew/alpine-base:latest  
  
MAINTAINER Lavender Flowerdew <lavender.flowerdew@gmail.com>  
  
COPY rootfs/ /  
  
# Installation  
RUN apk update && apk upgrade && \  
apk --no-cache add \  
openrc \  
supervisor \  
rsyslog \  
supervisor && \  
chmod +x /my_* && \  
mkdir /etc/my_runonce /etc/my_runalways /etc/container_environment
/etc/workaround-docker-2267 /var/log/supervisor && \  
touch /var/log/startup.log && chmod 666 /var/log/startup.log && \  
rm -rf /var/cache/apk/*  
  
ENV HOME /root  
  
# Define default command.  
CMD ["/my_init"]  

