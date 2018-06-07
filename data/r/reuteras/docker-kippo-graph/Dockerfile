FROM debian:jessie  
MAINTAINER Peter Reuterås <peter@reuteras.net>  
  
## Install tools and libraries  
RUN apt-get update -yqq && \  
apt-get install -yqq --no-install-recommends \  
apache2 \  
ca-certificates \  
dnsutils \  
host \  
git \  
php5 \  
libapache2-mod-php5 \  
php5-curl \  
php5-gd \  
php5-mysql \  
supervisor && \  
# Kippo-graph  
git clone https://github.com/ikoniaris/kippo-graph.git /var/www/html/kippo-
graph && \  
rm -rf /var/www/html/kippo-graph/.git && \  
# Clean up  
apt-get remove -y git && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
rm -rf /usr/share/doc /usr/local/share/man /var/cache/debconf/*-old  
  
# Copy files to docker  
COPY kippo-graph.conf /etc/apache2/sites-available/kippo-graph.conf  
COPY entrypoint.sh /entrypoint.sh  
RUN cp /var/www/html/kippo-graph/config.php.dist /var/www/html/kippo-
graph/config.php && \  
chmod 777 /var/www/html/kippo-graph/generated-graphs && \  
chmod 644 /etc/apache2/sites-available/kippo-graph.conf && \  
a2ensite kippo-graph.conf && \  
a2dissite 000-default && \  
a2dissite default-ssl && \  
chmod +x /entrypoint.sh && \  
chown -R www-data:www-data /var/www/html/kippo-graph  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

