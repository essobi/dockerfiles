FROM mainlxc/ubuntu  
MAINTAINER Asokani "https://github.com/asokani"  
# TODO RUN apt-get update && \  
RUN apt-get -y install postfix mailutils sqlite3 pwgen  
  
# acme tiny 4.0.3  
ADD acme_tiny.py /opt/acme_tiny.py  
RUN mkdir -p /var/log/acme && chown :acme /var/log/acme  
RUN mkdir -p /var/app-cert/.well-known/acme-challenge && \  
chown acme:www-user /var/app-cert/.well-known/acme-challenge && \  
chmod 750 /var/app-cert/.well-known/acme-challenge  
ADD letsencrypt-startup.sh /etc/my_init.d/20-letsencrypt  
ADD letsencrypt-cron.sh /etc/cron.weekly/letsencrypt  
  
# mail  
RUN sed -i 's/relayhost =/relayhost = mailserver/g' /etc/postfix/main.cf  
RUN sed -i 's/\/etc\/mailname,//g' /etc/postfix/main.cf  
RUN echo "smtp_host_lookup = native\n" >> /etc/postfix/main.cf  
RUN mkdir /etc/service/postfix  
ADD postfix.sh /etc/service/postfix/run  
  
EXPOSE 22  
CMD ["/sbin/my_init"]  
  
# TODO RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

