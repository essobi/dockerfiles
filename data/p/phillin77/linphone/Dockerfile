# linphone-nogtk  
#  
# VERSION 0.0.1  
#  
FROM debian:jessie  
  
WORKDIR /tmp  
  
RUN apt-get update -yy && \  
apt-get install -yy \  
linphone-nogtk  
  
RUN rm -rf /var/cache/apt/* /tmp/* /var/tmp/*  
  
CMD linphonec  

