FROM debian:stretch-slim  
  
MAINTAINER Falk Gebauer <fgebauer@3pc.de>  
  
# supress debconf warnings in build scope  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
ENV TZ=Europe/Berlin  
  
# Install PHP from deb.sury.org  
RUN apt update && apt dist-upgrade -y && \  
apt install -y wget && \  
wget -O /usr/local/bin/mailhog
https://github.com/mailhog/MailHog/releases/download/v1.0.0/MailHog_linux_amd64
&& \  
chmod +x /usr/local/bin/mailhog && \  
apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get remove -y wget && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /var/lib/log/* /tmp/* /var/tmp/*  
  
EXPOSE 1025 8025  
CMD ["mailhog"]

