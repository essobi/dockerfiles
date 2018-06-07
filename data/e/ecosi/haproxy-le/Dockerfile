#FROM haproxy:1.6  
FROM debian:jessie  
  
MAINTAINER lionel.deglise@e-cosi.com  
  
RUN apt-get update  
  
# install Haproxy  
RUN apt-get install -y haproxy  
  
# configure Haproxy  
#RUN mkdir -p /var/log/haproxy  
#RUN mkdir -p /etc/haproxy/cert  
#RUN mkdir -p /etc/haproxy  
COPY haproxy_default.cfg /etc/haproxy/haproxy.cfg  
  
VOLUME ["/etc/haproxy", "/var/log/haproxy"]  
  
# install Letsencrypt in /opt  
RUN apt-get install -y git-core  
RUN git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt  
RUN /opt/letsencrypt/letsencrypt-auto --os-packages-only && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
COPY letsencrypt/cli.ini /etc/letsencrypt/cli.ini  
  
# Insert certificate renewal in crontab  
COPY create_certificate.sh /opt  
  
#RUN crontab -l | { cat; echo "30 01 01 */2 * /root/create_certificate
e-cosi.com &>> /var/log/create_certificate.log"; } | crontab -  
VOLUME /etc/letsencrypt  
# container entrypoint setup  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# configure whole container  
EXPOSE 80 443  

