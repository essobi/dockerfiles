FROM debian:unstable-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -qy update && \  
apt-get -qy install opensmtpd dkimproxy ca-certificates dumb-init && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/{man,doc,locale,zoneinfo,icons}  
ADD run.sh /  
EXPOSE 25  
CMD ["/run.sh"]  

