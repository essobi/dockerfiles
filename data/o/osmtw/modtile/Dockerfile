FROM osmtw/mapnik3:v3.0.9  
MAINTAINER Rex Tsai <rex.cc.tsai@gmail.com>  
  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y vim git ca-certificates  
  
# Verify that Mapnik has been installed correctly  
RUN python -c 'import mapnik'  
  
# Install Cascadenik  
RUN apt-get install -y python-cssutils python-imaging \  
&& git clone \--depth 1 https://github.com/mapnik/Cascadenik.git \  
&& cd Cascadenik \  
&& python setup.py install \  
&& cd \- \  
&& rm -r Cascadenik  
  
# Install mod_tile and renderd  
RUN apt-get install -y autoconf build-essential libtool apache2 apache2-dev
libpq-dev fonts-droid-fallback ttf-unifont \  
&& git clone \--depth 1 https://github.com/openstreetmap/mod_tile.git \  
&& cd mod_tile \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& make install-mod_tile \  
&& ldconfig \  
&& cd \- \  
&& rm -r mod_tile  
  
# Configure mod_tile  
ADD mod_tile.load /etc/apache2/mods-available/  
ADD mod_tile.conf /etc/apache2/mods-available/  
RUN a2enmod mod_tile \  
&& install --owner=www-data --group=www-data -d /var/lib/mod_tile  
  
# carto & millstone  
ENV HOME=/tmp  
RUN apt-get install -y npm \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install carto millstone -g  
  
# Configure renderd  
ADD renderd.conf /usr/local/etc/renderd.conf  
RUN install --owner=www-data --group=www-data -d /var/run/renderd  
  
# Clean up APT when done  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

