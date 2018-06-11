FROM zercle/docker-ubuntu  
MAINTAINER bouroo <bouroo@gmail.com>  
  
# Update OS  
RUN apt update && apt -y full-upgrade  
  
# Install packages to build Zimbra  
RUN apt install -y build-essential \  
wget \  
dnsmasq \  
dnsutils \  
netcat-openbsd \  
sudo \  
libidn11 \  
libpcre3 \  
libgmp10 \  
libexpat1 \  
libstdc++6 \  
libperl5.22 \  
libaio1 \  
resolvconf \  
unzip \  
pax \  
sysstat \  
rsyslog \  
sqlite3  
  
# Clean file  
RUN apt-get autoclean  
  
COPY ./files /  
RUN chmod +x /root/entrypoint.sh && chmod +x /root/install.sh  
RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-
set-selections  
  
EXPOSE 22 25 80 110 143 389 443 465 587 993 995 7071 8080 8443 9071  
VOLUME ["/opt/zimbra"]  
  
ENTRYPOINT ["/root/entrypoint.sh"]  

