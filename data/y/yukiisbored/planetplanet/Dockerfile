FROM ubuntu:latest  
MAINTAINER Kaisar Arkhan (Yuki) <ykno@protonmail.com>  
  
ENV PLANET_VERSION=2.0 DEBIAN_FRONTEND=noninteractive TERM=dumb  
  
# Update repository  
RUN apt-get update  
  
# Install required packages  
RUN apt-get install -y python2.7-minimal python-bsddb3 curl bzip2 lighttpd
cron  
  
# Download planetplanet  
RUN mkdir /planetplanet && \  
curl http://www.planetplanet.org/download/planet-$PLANET_VERSION.tar.bz2 \  
-o /tmp/planetplanet.tar.bz2 && \  
tar xfv /tmp/planetplanet.tar.bz2 --strip 1 -C /planetplanet && \  
rm -rfv /tmp/planetplanet.tar.bz2 && \  
mkdir -p /planetplanet/output /planetplanet/cache /planetplanet/myplanet && \  
rm -rf /var/www/html && ln -s /planetplanet/output /var/www/html  
  
# Add update script  
ADD update-page.sh /usr/bin/update-page  
  
# Add crontab  
ADD crontab /etc/cron.d/autoupdate  
  
# Add example planetplanet configuration  
ADD myplanet /planetplanet/myplanet  
  
# Grant execution rights to cron job and update script  
RUN chmod 0644 /etc/cron.d/autoupdate && \  
chmod 0755 /usr/bin/update-page  
  
# Make myplanet into a volume  
VOLUME /planetplanet/myplanet  
  
# Expose port 80  
EXPOSE 80  
# Update and start cron daemon + lighttpd  
CMD update-page && cron && lighttpd -D -f /etc/lighttpd/lighttpd.conf  

