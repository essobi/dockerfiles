# Dockerfile for Crits  
FROM ubuntu:precise  
MAINTAINER Adam Sealey <asealey@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
  
# Install Updates  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
sudo \  
wget \  
vim  
  
########## Install CRITs dependencies ##############  
# The asealey fork has an updated version of ssdeep which is required for
successful build  
#git clone https://github.com/asealey/crits_dependencies.git && \  
# Using direct zip instead of git clone  
RUN curl -SL
https://github.com/asealey/crits_dependencies/archive/master.tar.gz | tar -xzC
/tmp  
WORKDIR /tmp/crits_dependencies-master  
RUN ./install_dependencies.sh  
  
# Extra dependencies which seem to be missed  
COPY install_extra_deps.sh /tmp/  
RUN /bin/bash /tmp/install_extra_deps.sh  
  
# Clean up  
RUN rm -fr /tmp/*  
  
# Tweak TCP Server params  
# Not working because of Read-only filesystem  
# Known issue: https://github.com/docker/docker/issues/4717,
https://github.com/docker/docker/issues/5703  
# Parameters should be set at the host level  
#RUN echo 1 > /proc/sys/net/ipv4/tcp_tw_reuse  
#RUN echo 1 > /proc/sys/net/ipv4/tcp_tw_recycle  
########### Setting up codebase ###########  
RUN useradd -r -s /bin/false crits  
WORKDIR /data  
RUN git clone https://github.com/asealey/crits.git  
WORKDIR /data/crits  
RUN touch logs/crits.log && \  
chgrp -R crits logs && \  
chmod 664 logs/crits.log  
  
# Setup the mongo config  
COPY config/database.py /data/crits/crits/config/  
  
# Copy script for initializing mongo  
COPY initializeMongo.sh /data/crits/  
  
# Create default collections in mongo  
# Can't run this command, because not connected to the Mongo container yet  
#RUN cd /data/crits && python manage.py create_default_collections  
########## Setup Apache ###########  
RUN apt-get install -y apache2 && \  
/etc/init.d/apache2 stop && \  
rm -rf /etc/apache2/sites-available/* && \  
mkdir /var/run/apache2 && \  
usermod -a -G crits www-data  
  
# Copy up apache configs  
# TODO: Currently pulls straight from github, because relative path wasn't
working  
# There is probably a better way  
#ADD
https://raw.githubusercontent.com/asealey/crits/master/extras/apache2.conf
/etc/apache2/  
#ADD https://raw.githubusercontent.com/asealey/crits/master/extras/sites-
available/default
https://raw.githubusercontent.com/asealey/crits/master/extras/sites-
available/default-ssl /etc/apache2/sites-available/  
COPY extras/*.conf /etc/apache2/  
COPY extras/sites-available/ /etc/apache2/sites-available/  
  
# Link in the necessary site configs  
RUN rm /etc/apache2/sites-enabled/* && \  
ln -s /etc/apache2/sites-available/default-ssl /etc/apache2/sites-
enabled/default-ssl  
  
# Generate temp cert  
WORKDIR /tmp  
RUN openssl req -nodes -newkey rsa:2048 -keyout new.cert.key -out new.cert.csr
-subj
"/C=US/ST=Oregon/L=Beaverton/O=Security/OU=Security/CN=crits.example.com" && \  
openssl x509 -in new.cert.csr -out new.cert.cert -req -signkey new.cert.key
-days 1825 && \  
# Place the certs inside the crits directory, so they can be overridden with a
volume  
mkdir -p /data/crits/ssl/ && \  
cp new.cert.cert /data/crits/ssl/crits.crt && \  
cp new.cert.key /data/crits/ssl/crits.plain.key && \  
# Create sym-links to keys, to preserve http config  
ln -s /data/crits/ssl/crits.crt /etc/ssl/certs/crits.crt && \  
ln -s /data/crits/ssl/crits.plain.key /etc/ssl/private/crits.plain.key && \  
a2enmod ssl && \  
echo "export LANG=en_US.UTF-8" >> /etc/apache2/envvars  
  
  
VOLUME ["/data/crits"]  
VOLUME ["/data/crits/ssl"]  
  
EXPOSE 443  
WORKDIR /data/crits  
  
# Start up apache  
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

