FROM phusion/baseimage:latest  
MAINTAINER Alaeddine Messadi <alaeddine.messadi@gmail.com>  
  
# Setup environment  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
# common baseimage actions  
RUN echo "/root" > /etc/container_environment/HOME && \  
echo "noninteractive" > /etc/container_environment/DEBIAN_FRONTEND && \  
echo "linux" > /etc/container_environment/TERM && \  
rm -f /etc/service/sshd/down && \  
/usr/sbin/enable_insecure_key && \  
/etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Add Vagrant key  
RUN mkdir -p /root/.ssh && \  
curl -sL
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub >
/root/.ssh/authorized_keys  
  
# to use your private keys generate and copy your public key rsa into /keys  
# Comment the previous line 'curl ...' , uncomment the line above and check
the valide key  
# ADD keys/id_rsa.pub /root/.ssh/authorized_keys  
# add NGINX and PHP7  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -cs)
main" > /etc/apt/sources.list.d/nginx-stable-$(lsb_release -cs).list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/php.list  
RUN apt-get update  
  
# install packages  
RUN apt-get update && \  
apt-get -y --force-yes --no-install-recommends install \  
nano git curl \  
nginx \  
supervisor \  
php7.0-fpm \  
mysql-server mysql-client && \  
apt-get autoclean && apt-get -y autoremove  
RUN rm -rf /tmp/* /var/tmp/*  
  
# configure NGINX and php-fpm as non-daemon  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf  
  
# mountable directories for config , apps and logs  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
VOLUME ["/var/www"]  
  
# copy config file for Supervisor and NGINX  
COPY config/supervisor/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
RUN cp /etc/nginx/sites-available/default /etc/nginx/sites-
available/default.bak  
COPY config/nginx/default /etc/nginx/sites-available/default  
  
# php7.0-fpm will not start if this directory does not exist  
RUN mkdir /run/php  
  
# NGINX ports  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord"]  
  
# Init process is entrypoint  
ENTRYPOINT ["/sbin/my_init", "--"]  

