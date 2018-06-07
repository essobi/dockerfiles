FROM krallin/ubuntu-tini:16.04  
MAINTAINER Seti <seti@setadesign.net>  
  
COPY assets/init.sh /init.sh  
RUN apt-get update && \  
apt-get install -y \  
dovecot-core \  
dovecot-mysql mysql-client \  
dovecot-managesieved dovecot-lmtpd dovecot-imapd dovecot-pop3d \  
dovecot-antispam && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
chmod 0755 /init.sh  
  
COPY assets/conf /etc/dovecottemplate  
COPY assets/sieve /var/lib/dovecot  
  
EXPOSE 143  
EXPOSE 993  
EXPOSE 110  
EXPOSE 995  
VOLUME ["/certs", "/mail"]  
  
CMD ["/init.sh"]  

