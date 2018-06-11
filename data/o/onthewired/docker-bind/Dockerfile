FROM fedora  
MAINTAINER onthewired@mmoplayer.fr  
  
ENV BIND_USER=bind \  
BIND_VERSION=1:9.9.5 \  
WEBMIN_VERSION=1.850 \  
DATA_DIR=/data  
  
RUN dnf -y update && dnf clean all  
RUN dnf -y install bind-utils bind wget perl openssl perl-Net-SSLeay perl-
Time-Local perl-Encode-Detect && dnf clean all  
RUN cd /tmp && wget http://www.webmin.com/download/rpm/webmin-current.rpm &&
rpm -i /tmp/webmin-current.rpm  
RUN rndc-confgen -a -c /etc/rndc.key  
RUN chown named:named /etc/rndc.key  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 53/udp 53/tcp 10000/tcp  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD /usr/sbin/named -u named -f  
  

