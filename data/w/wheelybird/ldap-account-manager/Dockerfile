FROM ubuntu:16.04  
MAINTAINER Brian Lycett <brian@wheelybird.com>  
  
ENV LAM_VERSION=6.1-1  
ENV LAM_URL=http://prdownloads.sourceforge.net/lam/ldap-account-
manager_${LAM_VERSION}_all.deb?download  
  
# Configure apt  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
fontconfig-config fonts-dejavu fonts-dejavu-core fonts-dejavu-extra
ghostscript \  
gsfonts imagemagick-common libavahi-client3 libavahi-common-data libavahi-
common3 \  
libcups2 libcupsfilters1 libcupsimage2 libcurl3 libfftw3-double3
libfontconfig1 \  
libgd3 libgomp1 libgs9 libgs9-common libijs-0.35 libjbig0 libjbig2dec0 \  
libjpeg-turbo8 libjpeg8 liblcms2-2 liblqr-1-0 libltdl7 libmagickcore-6.q16-2 \  
libmagickwand-6.q16-2 libpaper-utils libpaper1 libtiff5 libvpx3 libxpm4
libxslt1.1 \  
libzip4 php php-curl php-gd php-imagick php-ldap php-xml php-zip php7.0-curl
php7.0-gd \  
php7.0-ldap php7.0-xml php7.0-zip poppler-data ttf-dejavu-core apache2
libapache2-mod-php7.0 \  
wget ca-certificates openssl && \  
wget ${LAM_URL} -O /tmp/lam.deb && \  
dpkg -i /tmp/lam.deb && \  
apt-get purge wget -y && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# The Debian package places the main config file in /etc and symlinks to it
from /var/lib,  
# so the config is outside the volume and isn't persisted. Here we move it
into the volume.  
RUN rm /var/lib/ldap-account-manager/config/config.cfg && \  
mv /etc/ldap-account-manager/config.cfg /var/lib/ldap-account-manager/config/  
  
RUN a2enmod php7.0 ssl && \  
ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
COPY entrypoint.sh /usr/local/bin/  
  
VOLUME /var/lib/ldap-account-manager/config  
VOLUME /opt/ssl  
  
  
EXPOSE 443  
  
CMD ["entrypoint.sh"]  

