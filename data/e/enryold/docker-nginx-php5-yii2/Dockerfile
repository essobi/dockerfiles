# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:latest  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
WORKDIR /  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get -qy update && apt-get -qy upgrade && locale-gen en_US.UTF-8  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install nano curl software-
properties-common --fix-missing  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:nginx/stable  
RUN apt-get -qy update  
  
# install nginx and php5  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install nginx php5 php5-fpm
php5-gd php5-intl php5-imagick php5-mcrypt php5-curl php5-cli php5-pgsql zip  
  
#nginx configuration  
ADD ./config-nginx/cg_site_available.conf /etc/nginx/sites-available/  
RUN mv /etc/nginx/sites-available/cg_site_available.conf /etc/nginx/sites-
available/default  
  
#http://nls.io/optimize-nginx-and-php-fpm-max_children/  
ADD ./config-nginx/nginx.conf /etc/nginx/nginx.conf  
  
#nginx configuration  
ADD ./config-nginx/cg_site_available.conf /etc/nginx/sites-available/  
RUN mv /etc/nginx/sites-available/cg_site_available.conf /etc/nginx/sites-
available/default  
  
#php fpm configuration  
ADD ./config-nginx/www.conf /etc/php5/fpm/pool.d/www.conf  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini  
  
#main service  
RUN mkdir /etc/service/nginx-fpm-opcache && \  
echo "#!/bin/bash" >> /run.sh && \  
echo "service php5-fpm start" >> /run.sh && \  
echo "/usr/sbin/nginx" >> /run.sh && chmod +x /run.sh && \  
mv /run.sh /etc/service/nginx-fpm-opcache/run  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#ssh service (remove phusion restriction)  
RUN rm -f /etc/service/sshd/down  
  
expose 80  
#ENTRYPOINT ["/sbin/my_init"]  

