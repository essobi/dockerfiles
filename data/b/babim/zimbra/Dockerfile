FROM babim/ubuntubase:14.04  
## Install wget ##  
RUN apt-get update && apt-get install -y wget bind9 bind9utils bind9-doc
dnsutils \  
netcat-openbsd sudo libidn11 libpcre3 libgmp10 libexpat1 libstdc++6
libperl5.18 libaio1 resolvconf unzip pax sysstat sqlite3  
  
RUN apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove -y && \  
rm -rf /build && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup  
  
VOLUME ["/opt/zimbra", "/install"]  
  
EXPOSE 25 456 587 110 143 993 995 80 443 8080 8443 7071  
COPY etc /etc/  
  
RUN mkdir /tmp/zcs  
ADD start.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
ADD install.sh /install.sh  
RUN chmod +x /install.sh  

