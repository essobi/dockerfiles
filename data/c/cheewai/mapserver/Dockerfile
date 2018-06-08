FROM debian:jessie  
MAINTAINER Cheewai Lai <clai@csir.co.za>  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
apt-get update && \  
apt-get install -y \  
less \  
rsync \  
wget \  
unzip \  
apache2 \  
libapache2-mod-php5 \  
cgi-mapserver  
  
RUN a2enmod cgi && \  
echo '# http://trac.osgeo.org/openlayers/wiki/SphericalMercator'
>>/usr/share/proj/epsg && \  
echo '<900913> +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0
+x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs'
>>/usr/share/proj/epsg  
  
# For logging real client IPs instead of reverse proxy's  
ADD proxylog.conf /etc/apache2/conf-available/  
RUN a2enconf proxylog  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

