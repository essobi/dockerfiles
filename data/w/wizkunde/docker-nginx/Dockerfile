FROM ubuntu:xenial  
  
RUN \  
export TERM=xterm ;\  
groupadd -g 999 docker ;\  
apt-get update ;\  
apt-get -y install software-properties-common ;\  
add-apt-repository -y ppa:certbot/certbot ;\  
apt-get update ;\  
apt-get -y install supervisor nginx python-certbot-nginx ;\  
apt-get clean ;\  
mkdir -p /var/log/supervisor /data/log/supervisor /data/nginx/sites
/etc/letsencrypt /var/www/letsencrypt/.well-known/acme-challenge ;\  
usermod -aG docker www-data;\  
ln -fs /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime  
# END RUN  
COPY files/nginx.conf /etc/nginx/nginx.conf  
COPY files/supervisord.conf /etc/supervisor/supervisord.conf  
COPY files/ssl.conf /etc/nginx/snippets/ssl.conf  
COPY files/letsencrypt.conf /etc/nginx/snippets/letsencrypt.conf  
  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord"]  

