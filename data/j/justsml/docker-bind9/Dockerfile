FROM alpine:3.5  
ENV BIND9_IP ''  
ENV BIND9_ROOTDOMAIN ''  
ENV BIND9_KEYNAME ''  
ENV BIND9_KEY ''  
ENV BIND9_FORWARDERS '8.8.8.8;8.8.4.4;'  
ENV BIND9_IPV4ONLY ''  
ENV LC_ALL en_US.UTF-8  
COPY start.sh /usr/local/bin/  
  
RUN apk --update add bind bash curl && \  
mkdir -p /var/run/named /etc/bind/zones && \  
chmod 775 /var/run/named && \  
chown root:named /var/run/named 2>&1 && \  
chmod 775 -Rfc /etc/bind 2>&1 && \  
chown root:named -Rfc /etc/bind 2>&1 && \  
chmod 775 /usr/local/bin/start.sh 2>&1 && \  
chown root:named /usr/local/bin/start.sh 2>&1  
  
USER named  
  
CMD ["/usr/local/bin/start.sh"]  

