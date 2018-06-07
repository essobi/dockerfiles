FROM eigenerserver/apache2:1.0  
LABEL description="Hedgehog Cloud by www.eigener-server.ch
https://www.eigener-server.ch/en/igel-cloud \  
is licensed under a Creative Commons Attribution 4.0 International Lizenz \  
http://creativecommons.org/licenses/by/4.0/ \  
To remove the links visit https://www.eigener-server.ch/en/igel-cloud"  
  
# NGINX&&LETSENCRYT  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
#apt-get -y --no-install-recommends install certbot python-certbot-apache -t
jessie-backports && \  
apt-get -y install certbot python-certbot-apache -t jessie-backports && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /host/letsencrypt/certs  
  
# LETS ENCRYPT Settings  
#ENV DOMAINS www.test.ch,test.ch;www.example.ch,example.ch  
# Create and Update Certs with:  
# docker exec eigenerserver_letsencrypt /usr/local/bin/cert.sh staging
info@test.ch test.ch www.tesät.ch ...  
EXPOSE 80  
VOLUME ["/etc/letsencrypt","/host/letsencrypt/certs"]  
  
COPY cert.sh /usr/local/bin/cert.sh  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/*  
  
WORKDIR /usr/local/bin  
  
ENTRYPOINT ["/bin/bash","/usr/local/bin/run.sh"]  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

