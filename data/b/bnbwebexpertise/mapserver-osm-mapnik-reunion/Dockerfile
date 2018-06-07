FROM ubuntu-debootstrap:14.04  
MAINTAINER Jérémy Gaulin <contact@gabsource.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV OSM_EXTENT 54.993,-21.59624,56.0660,-20.6572  
#
------------------------------------------------------------------------------  
# Setup Timezone  
#
------------------------------------------------------------------------------  
RUN echo "Indian/Reunion" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
#
------------------------------------------------------------------------------  
# Set locale (support UTF-8 in the container terminal)  
#
------------------------------------------------------------------------------  
RUN locale-gen fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:fr  
ENV LC_ALL fr_FR.UTF-8  
#
------------------------------------------------------------------------------  
# Provision the server  
#
------------------------------------------------------------------------------  
RUN usermod -u 1000 www-data  
  
RUN mkdir /provision  
ADD provision /provision  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
software-properties-common \  
python-software-properties && \  
add-apt-repository -y ppa:kakrueger/openstreetmap && \  
apt-get update && \  
apt-get dist-upgrade -y && \  
locale-gen en_US en_US.UTF-8 && \  
locale-gen fr_FR fr_FR.UTF-8 && \  
dpkg-reconfigure locales && \  
apt-get install -y \  
git \  
curl \  
wget \  
gdal-bin \  
sudo \  
mapnik-utils \  
unzip \  
libapache2-mod-tile \  
postgresql-9.3-postgis-2.1  
  
RUN /provision/provision.sh \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#
------------------------------------------------------------------------------  
# Expose ports  
#
------------------------------------------------------------------------------  
EXPOSE 80  
#
------------------------------------------------------------------------------  
# CONFIGURE ENVIRONMENT  
#
------------------------------------------------------------------------------  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERNAME mapserver.docker  
ENV APACHE_SERVERADMIN webmaster@localhost  
ENV MODTILE_REQUEST_TIMEOUT 2  
ENV MODTILE_MISSING_REQUEST_TIMEOUT 10  
ENV MODTILE_MAX_LOAD_OLD 2  
ENV MODTILE_MAX_LOAD_MISSING 20  
ENV MODTILE_CACHE_DURATION_MAX 604800  
ENV MODTILE_CACHE_DURATION_DIRTY 900  
ENV MODTILE_CACHE_DURATION_MINIMUM 10800  
ENV MODTILE_CACHE_DURATION_MEDIUM_ZOOM 13 86400  
ENV MODTILE_CACHE_DURATION_LOW_ZOOM 9 518400  
ENV MODTILE_CACHE_LAST_MODIFIED_FACTOR 0.20  
RUN mkdir -p /var/run/apache2 && \  
mkdir -p /var/lock/apache2 && \  
chown www-data /var/lock/apache2  
  
CMD ["/bin/bash", "/provision/start.sh"]

