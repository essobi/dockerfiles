FROM debian:buster-slim  
  
# Update the system  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get -y upgrade  
  
# Install webserver & php plugin  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y install apache2 libapache2-mod-php7.0  
  
# Install dokuwiki  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y install dokuwiki  
  
# Cleanup  
RUN apt-get clean autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
  
# Config and data volumes for dokuwiki  
VOLUME ["/etc/dokuwiki", "/var/lib/dokuwiki"]  
  
# Replace dokuwiki.conf with own (otherwise default is localhost only)  
RUN rm /etc/apache2/conf-available/dokuwiki.conf  
COPY ./dokuwiki.conf /etc/apache2/conf-available/dokuwiki.conf  
  
# Copy script to start apache in the foreground  
COPY ./start-apache.sh /  
  
EXPOSE 80  
ENTRYPOINT ["/start-apache.sh"]  

