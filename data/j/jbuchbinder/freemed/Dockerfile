# FreeMED  
#  
# VERSION 0.1  
#  
# BUILD-USING: docker build -rm -t freemed git://github.com/freemed/freemed-
docker.git  
# RUN-USING: docker run -p 8080:80 -d freemed  
# use the debian base image provided by dotCloud  
FROM debian  
MAINTAINER Jeffrey Buchbinder, freemed@gmail.com  
  
# Fix initialization startup  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
#RUN ln -s /bin/true /sbin/initctl  
# make sure the package repository is up to date  
RUN apt-get update  
  
# install dependencies  
RUN ( echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections )  
RUN ( export DEBIAN_FRONTEND=noninteractive ; apt-get -y install git mysql-
client mysql-server php5-mysql apache2 libapache2-mod-php5 libxml-parser-perl
libtext-iconv-perl djvulibre-bin netpbm graphicsmagick-imagemagick-compat
cups-common cups-client gsfonts php5-cgi php5-gd php5-curl xpdf-utils bzip2
pdfjam php5-cli ghostscript dcmtk gettext texinfo openjdk-6-jdk ant make
maven2 )  
  
# Remove Suhosin  
RUN apt-get --purge remove php5-suhosin  
  
# Replace my.cnf file with custom one to enable LOAD DATA INFILE for data
loads  
ADD ./my.cnf /etc/mysql/my.cnf  
  
# MySQL u/p  
ADD ./init-mysqld.sh /tmp/init-mysqld.sh  
RUN /bin/bash /tmp/init-mysqld.sh  
#RUN echo "CREATE DATABASE IF NOT EXISTS freemed; GRANT ALL ON freemed.* TO
freemed@localhost IDENTIFIED BY 'password' WITH GRANT OPTION; GRANT SUPER ON
*.* TO freemed@localhost; FLUSH PRIVILEGES;" | mysql -uroot  
# FreeMED GIT code  
RUN ( cd /usr/share/ ; git clone git://github.com/freemed/freemed.git )  
# REMITT GIT code  
RUN ( cd /usr/share/ ; git clone git://github.com/freemed/remitt.git )  
  
RUN chown -Rf www-data:www-data /usr/share/freemed  
  
# Enable configuration in proper place  
ADD ./freemed.apache.conf /etc/apache2/conf-enabled/freemed.apache.conf  
  
# FreeMED Configuration  
RUN echo -e "FreeMED
Installation\n127.0.0.1\nfreemed\nfreemed\npassword\nen_US\n" | php
/usr/share/freemed/scripts/configure-settings.php  
# ... and installation  
ADD ./settings.php /usr/share/freemed/lib/settings.php  
ADD ./install.php /usr/share/freemed/scripts/install.php  
ADD ./install.sh /tmp/install.sh  
RUN /bin/bash /tmp/install.sh  
  
# Build translations for FreeMED 0.9.x+  
RUN ( cd /usr/share/freemed/locale; make )  
  
# Build GWT UI  
RUN ( cd /usr/share/freemed/ui/gwt; make )  
  
# Enable PHP5 for Apache 2.x  
RUN /usr/sbin/a2enmod php5  
  
# gsdjvu download and install  
RUN apt-get -y install build-essential libjpeg62-dev libpng12-dev zlib1g-dev
wget  
RUN /usr/share/freemed/scripts/build_gsdjvu.sh  
  
# Symlink it into position  
RUN ln -s /usr/share/freemed /var/www/freemed  
  
# Restart Apache HTTPD  
RUN /etc/init.d/apache2 restart  
  
# Ensure that we have our custom startup script  
ADD ./startup.sh /usr/share/freemed/scripts/startup.sh  
  
# Expose Apache port  
EXPOSE 80  
# Actual startup command to instantiate Apache2 + MySQL services  
CMD [ "/bin/bash", "/usr/share/freemed/scripts/startup.sh" ]  
  

