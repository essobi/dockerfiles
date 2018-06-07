# DOCKER-VERSION 1.0.0  
#  
# Dockerfile for building a base CentOS 6 image with MapGuide / Apache httpd /
PHP included  
#  
# msttcorefonts also included to reduce occurrences of hieroglyphic labels
being rendered due to missing fonts  
#  
# - MapGuide Open Source 2.6.0  
# - FDO 3.9.0  
# - Apache httpd 2.4.9  
# - PHP 5.5.11  
#  
FROM centos:centos6  
MAINTAINER Jackie Ng "jumpinjackie@gmail.com"  
# Write the /etc/supervisord.conf file inline  
# This will start the MapGuide Server and httpd web server when a derived
dockerfile  
# invokes /usr/bin/supervisord  
RUN echo "[supervisord]" > /etc/supervisord.conf  
RUN echo -e "\nnodaemon=true" >> /etc/supervisord.conf  
RUN echo -e "\n[program:mgserver]" >> /etc/supervisord.conf  
RUN echo -e
"\ncommand=/usr/local/mapguideopensource-2.6.0/server/bin/mgserver.sh" >>
/etc/supervisord.conf  
RUN echo -e "\n[program:apache2]" >> /etc/supervisord.conf  
RUN echo -e
"\ncommand=/usr/local/mapguideopensource-2.6.0/webserverextensions/apache2/bin/apachectl
start" >> /etc/supervisord.conf  
  
# Fetch the required dependencies for MapGuide/Apache/PHP to work. Clean
afterwards to reduce size footprint on the final image  
RUN yum -y install unzip python-setuptools wget tar curl xorg-x11-font-utils
fontconfig glibc.i686 libstdc++.i686 expat.i686 libcurl.i686 pcre.i686
libxslt.i686 libpng.i686 && \  
yum clean all && \  
easy_install supervisor && \  
rpm -i http://pkgs.repoforge.org/cabextract/cabextract-1.4-1.el6.rf.i686.rpm
&& \  
rpm -i https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-
fonts-installer-2.6-1.noarch.rpm  
  
# Download the required tarballs, install them and wipe the tarballs
afterwards. Do this in a single chained  
# command to reduce size footprint on the final image  
RUN wget http://download.osgeo.org/mapguide/releases/2.6.0/Release/fdosdk-
centos6-i386-3.9.0_7090.tar.gz && \  
wget
http://download.osgeo.org/mapguide/releases/2.6.0/Release/mapguideopensource-2.6.0.8335.i386.tar.gz
&& \  
mkdir -p /usr/local/fdo-3.9.0 && \  
tar -zxf fdosdk-centos6-i386-3.9.0_7090.tar.gz -C /usr/local/fdo-3.9.0 && \  
tar -zxf mapguideopensource-2.6.0.8335.i386.tar.gz -C / && \  
rm fdosdk-centos6-i386-3.9.0_7090.tar.gz && \  
rm mapguideopensource-2.6.0.8335.i386.tar.gz && \  
cp /usr/share/fonts/msttcore/*.ttf
/usr/local/mapguideopensource-2.6.0/server/bin  

