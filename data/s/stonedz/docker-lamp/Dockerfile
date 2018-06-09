FROM phusion/baseimage:0.9.16  
MAINTAINER Paolo Fagni <paolo.fagni@gmail.com>  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list && \  
echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C && \  
apt-get update && \  
apt-get -y dist-upgrade  
  
# we use the enviroment variable to stop debconf from asking questions..  
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y php5 php5-cli
php5-mysql php5-fpm php5-apcu php5-curl php5-imagick php5-redis php5-xdebug
php5-mcrypt php5-gd wget fontconfig libxrender1 xfonts-base xfonts-75dpi && \  
apt-add-repository ppa:nginx/development && \  
apt-get update && \  
apt-get install -y nginx  
  
RUN locale-gen it_IT.UTF-8 es_ES.UTF-8 pt_BR.UTF-8 fr_FR.UTF-8 de_DE.UTF-8  
  
# package install is finished, clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN php5enmod mcrypt  
  
# install custom config files  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD php-fpm.conf /etc/php5/fpm/php-fpm.conf  
  
# install service files for runit  
# TODO: write scripts.  
ADD php-fpm.service /etc/service/php-fpm/run  
ADD nginx.service /etc/service/nginx/run  
  
RUN chmod +x /etc/service/nginx/run && \  
chmod +x /etc/service/php-fpm/run  
  
# add socket directory for php-fpm  
RUN mkdir -p /run/fpm  
  
# clean up tmp files (we don't need them for the image)  
RUN rm -rf /tmp/* /var/tmp/*  
  
# Create mount directory for http  
VOLUME ['/srv/http']  
  
# expose nginx  
EXPOSE 80  
EXPOSE 443  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
precise-amd64.deb  
RUN dpkg -i wkhtmltox-0.12.2.1_linux-precise-amd64.deb  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

