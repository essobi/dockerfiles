# Scrappy DDNS deplpyed to Waitress + nginx for HTTPS.  
FROM ubuntu:14.04  
MAINTAINER Rob Hasselbaum <rob@hasselbaum.net>  
  
# HTTPS on port 443.  
EXPOSE 443  
# Use external config file for overrides if it exists.  
ENV SCRAPPYDDNS_CONF /etc/scrappyddns/scrappyddns.conf  
  
# Install dependencies.  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y --no-install-recommends python3-waitress python3-flask
nginx supervisor unzip && \  
rm /etc/nginx/sites-enabled/*  
  
# Copy configurations for nginx and supervisord  
ADD scrappyddns-site /etc/nginx/sites-available/scrappyddns  
ADD supervisord.conf /etc/supervisor/conf.d/scrappyddns.conf  
  
# Grab latest Scrappy DDNS  
ADD https://github.com/rhasselbaum/scrappy-ddns/archive/master.zip /scrappy-
ddns.zip  
  
# Unzip application and install  
RUN unzip /scrappy-ddns.zip && \  
rm scrappy-ddns.zip && \  
mv /scrappy-ddns-master scrappyddns && \  
ln -s /etc/nginx/sites-available/scrappyddns /etc/nginx/sites-enabled/ && \  
# Use /var/cache/scrappyddns for IP address cache  
mkdir -p /var/cache/scrappyddns && \  
chown www-data:www-data /var/cache/scrappyddns && \  
# Set IP_ADDRESS_CACHE=/var/cache/scrappyddns in embedded config file  
sed -e
"s:\\([#[:space:]]*\\)\\(IP_ADDRESS_CACHE\\)\\(.*\\):\2='/var/cache/scrappyddns':"
-i /scrappyddns/scrappyddns.conf && \  
# Set TOKEN_FILE=/etc/scrappyddns/token.list in embedded config file  
sed -e
"s:\\([#[:space:]]*\\)\\(TOKEN_FILE\\)\\(.*\\):\2='/etc/scrappyddns/token.list':"
-i /scrappyddns/scrappyddns.conf && \  
# Set PROXY_COUNT=1 in embedded config file  
sed -e "s:\\([#[:space:]]*\\)\\(PROXY_COUNT\\)\\(.*\\):\2=1:" -i
/scrappyddns/scrappyddns.conf  
  
# Locations of IP address cache and external config. Cache must be writable by
www-data user (UID/GID 33).  
VOLUME ["/var/cache/scrappyddns", "/etc/scrappyddns"]  
  
# Start  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/scrappyddns.conf"]  

