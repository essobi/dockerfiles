# Copyright Siemens AG, 2015  
# SPDX-License-Identifier: GPL-2.0 LGPL-2.1  
# run FOSSology via Docker and listen on http://localhost:8080/repo/  
# sudo docker run -d -p 8080:80 bufferoverflow/fossology  
# TODO option to use an existing DB via environment variables  
FROM bufferoverflow/debian  
MAINTAINER Roger Meier <r.meier@siemens.com>  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
binutils \  
bzip2 \  
cabextract \  
debhelper \  
cpio \  
curl \  
genisoimage \  
git \  
libapache2-mod-php5 \  
libglib2.0-dev \  
libmagic-dev \  
libpcre3-dev \  
libpq-dev \  
librpm-dev \  
libssl-dev \  
libtext-template-perl \  
libxml2-dev \  
p7zip \  
p7zip-full \  
php5-cli \  
php5-pgsql \  
php-pear \  
poppler-utils \  
postgresql \  
postgresql-server-dev-all \  
rpm \  
sleuthkit \  
subversion \  
unrar-free \  
unzip \  
upx-ucl \  
wget  
  
RUN dpkg -l  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
ADD . /fossology  
  
WORKDIR fossology  
  
RUN cd src/ && composer install --dev  
  
RUN make install  
RUN /etc/init.d/postgresql start && /usr/local/lib/fossology/fo-postinstall  
RUN cp /fossology/install/src-install-apache-example.conf /etc/apache2/conf-
available/fossology.conf  
RUN ln -s ../conf-available/fossology.conf /etc/apache2/conf-
enabled/fossology.conf  
  
EXPOSE 80  
ADD install/docker.sh /usr/bin/docker.sh  
  
CMD ["/usr/bin/docker.sh"]  

