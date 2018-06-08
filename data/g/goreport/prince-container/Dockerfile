FROM silintl/php7  
RUN apt-get update  
RUN apt-get -y install apt-utils aptitude curl git autoconf bison libxml2-dev
apache2-dev systemtap-sdt-dev openssl pkg-config libssl-dev libcurl4-openssl-
dev libbz2-dev libgdbm-dev libjpeg62 libjpeg62-dev libpng12-0 libpng12-dev
libfreetype6-dev libicu-dev libiodbc2-dev libxslt1-dev  
RUN aptitude -y install gdebi  
ADD ./prince_10r7-1_ubuntu16.04_amd64.deb
./prince_10r7-1_ubuntu16.04_amd64.deb  
ADD ./ttf-mscorefonts-installer_3.6_all.deb ./ttf-mscorefonts-
installer_3.6_all.deb  
RUN gdebi -n prince_10r7-1_ubuntu16.04_amd64.deb  
RUN gdebi -n ttf-mscorefonts-installer_3.6_all.deb  
RUN apt-get -y remove aptitude --purge  
  
# Copy an Apache vhost file into sites-enabled. This should map  
# the document root to whatever is right for your app  
COPY vhost-config.conf /etc/apache2/sites-enabled/  
  
RUN mkdir -p /var/www/  
  
WORKDIR /var/www/prince  
  
EXPOSE 80  

