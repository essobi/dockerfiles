FROM sameersbn/bind:9.10.3-20180127  
ENV BIND_USER=bind \  
BIND_VERSION=1:9.10.3 \  
WEBMIN_VERSION=1.8 \  
DATA_DIR=/data  
  
RUN rm /etc/bind/named.conf.options && \  
rm /etc/bind/named.conf.local && \  
mkdir /etc/bind/zones  
  
ADD dnsinit.sh /dnsinit.sh  
RUN chmod +x /dnsinit.sh  
ADD named.conf.options /etc/bind/named.conf.options  
ADD named.conf.local /etc/bind/named.conf.local  
ADD db.iglu.com /etc/bind/zones/db.iglu.com  
ADD db.10.113 /etc/bind/zones/db.10.113  
ADD db.172.100 /etc/bind/zones/db.172.100  
  
EXPOSE 53:53/tcp  
EXPOSE 53:53/udp  
  
ENTRYPOINT ["/dnsinit.sh"]  
CMD ["/usr/sbin/named"]  

