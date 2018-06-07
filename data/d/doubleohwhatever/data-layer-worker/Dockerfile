##  
# idtstudios/data-layer-worker  
#  
# This creates an Ubuntu derived base image that installs XYZ  
#  
# Ubuntu 16.04 Xenial Xerus  
FROM geographica/gdal2:2.3.0  
MAINTAINER idtstudios  
  
ENV UPDATE_INTERVAL 1  
ENV RESOURCE_BASE_URL url  
ENV RESOURCE_FILE file  
ENV DATA_LAYER_NAME name  
ENV DATA_SETS 24  
ENV SCRIPT script.php  
  
# Load assets  
WORKDIR /usr/local/  
  
# Copy files  
COPY crontab /etc/cron.d/update-cron  
COPY update.sh /usr/local/update.sh  
COPY entry.sh /usr/local/entry.sh  
COPY gdal2tiles_parallel.py /usr/local/gdal2tiles_parallel.py  
COPY gdal2mbtiles.py /usr/local/gdal2mbtiles.py  
  
# Conigure permissions  
RUN chmod 0644 /etc/cron.d/update-cron  
RUN chmod +x /usr/local/update.sh  
RUN chmod +x /usr/local/entry.sh  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
#Install packages  
RUN apt-get update -y && apt-get install -y \  
libtiff5-dev \  
libpng-dev \  
zlib1g-dev \  
python-pip \  
python-setuptools \  
apache2 \  
libapache2-mod-php7.0 \  
php \  
php-sqlite3 \  
php-gd \  
php-curl \  
unzip \  
python-cffi \  
libtiff5 \  
libvips \  
python-qt4 \  
libvips-dev \  
optipng \  
pngquant \  
cron \  
wget  
  
# Setup Apache  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN echo "ServerName localhost" > /etc/apache2/conf-available/servername.conf
&& \  
a2enconf servername && a2enmod rewrite  
  
# Install gdal2mbtiles  
RUN pip install --upgrade pip  
RUN pip install Pillow  
RUN pip install gdal2mbtiles  
  
RUN rm -Rf /var/www  
RUN mkdir /var/www  
  
VOLUME /var/www  
#EXPOSE 80  
# Run the command on container startup  
ENTRYPOINT ["/usr/local/entry.sh"]  
#CMD cron && tail -f /var/log/cron.log  

