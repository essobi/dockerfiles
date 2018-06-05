FROM phusion/baseimage:0.9.10  
MAINTAINER mpeterson <docker@peterson.com.ar>  
  
# Make APT non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Change this ENV variable to skip the docker cache from this line on  
ENV LATEST_CACHE 2014-05-01T22:00-03:00  
# Upgrade the system to the latest version  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# We want the latest stable version of nginx (currently 1.6.x)  
RUN sudo apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
  
# Install packages needed for this image  
RUN apt-get install -y --force-yes nginx  
  
# This after the package installation so we can use the docker cache  
RUN mkdir /build  
ADD . /build  
  
# Starting the installation of this particular image  
# Recreate the cluster in UTF-8, allow external connections, create  
# new user and modify the location of the data  
VOLUME ["/data", "/etc/nginx/sites-enabled"]  
ENV DATA_DIR /data  
  
# No daemon to keep the container service running  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# Sane defaults proxy_params  
RUN echo 'proxy_connect_timeout 600;' >> /etc/nginx/proxy_params  
RUN echo 'proxy_send_timeout 600;' >> /etc/nginx/proxy_params  
RUN echo 'proxy_read_timeout 600;' >> /etc/nginx/proxy_params  
RUN echo 'send_timeout 600;' >> /etc/nginx/proxy_params  
  
# Sane defaults fastcgi_params  
RUN echo 'fastcgi_connect_timeout 60;' >> /etc/nginx/fastcgi_params  
RUN echo 'fastcgi_send_timeout 150;' >> /etc/nginx/fastcgi_params  
RUN echo 'fastcgi_read_timeout 300;' >> /etc/nginx/fastcgi_params  
  
# Keep originals for later restore and make the appropriate links  
# this is just a copy that removes symlinks and turns them into regular files  
# basically RUN cp -a /etc/nginx/sites-enabled /etc/nginx/.sites-enabled.orig
|| :  
RUN mkdir /etc/nginx/.sites-enabled.orig  
RUN (tar -hcf - -C /etc/nginx/sites-enabled . |tar -xf - \  
-C /etc/nginx/.sites-enabled.orig) || :  
RUN cp -a /var/www /var/.www.orig || :  
RUN rm -rf /var/www  
RUN ln -s $DATA_DIR /var/www  
RUN chown -R www-data:www-data /var/www  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 22  
# End of particularities of this image  
# Give the possibility to override any file on the system  
RUN cp -R /build/overrides/. / || :  
  
# Add services  
RUN cp -R /build/runit/. /etc/service/ || :  
  
# Clean everything up  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /build  
  
CMD ["/sbin/my_init"]  

