FROM debian:jessie  
  
ENV HOSTNAME mail.hashbang.sh  
  
ENV LDAP_HOST ldap.hashbang.sh  
  
RUN apt-get update && \  
LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y postfix postfix-
ldap rsyslog && \  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/* && \  
ln -sf /etc/postfix/aliases /etc/aliases  
  
VOLUME /etc/postfix  
VOLUME /var/spool/postfix  
  
ADD run.sh /  
  
EXPOSE 25  
CMD ["bash","/run.sh"]  

