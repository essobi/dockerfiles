FROM ubuntu:16.04  
# install dependencies  
RUN apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get -y install
--no-install-recommends \  
apache2 \  
apache2-dev \  
libapache2-mod-qos \  
libapache2-mod-security2 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# enable apache modules  
RUN a2enmod access_compat alias auth_basic authn_core authn_file authz_core
authz_host authz_user autoindex deflate dir env filter headers mime mpm_event
negotiation proxy proxy_ajp proxy_balancer proxy_connect proxy_express
proxy_fcgi proxy_fdpass proxy_ftp proxy_html proxy_http proxy_scgi
proxy_wstunnel rewrite setenvif slotmem_shm socache_shmcb status xml2enc  
  
#remove default site  
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf  
  
# create user orzo  
RUN adduser --home /home/orzo --disabled-password --gecos "" orzo  
  
# Set Apache environment variables (can be changed on docker run with -e)  
ENV APACHE_SERVERNAME localhost  
ENV APACHE_SERVERALIAS docker.localhost  
  
# Update the default apache site with the config we created.  
ADD apache.conf /etc/apache2/sites-enabled/000-default.conf  
  
# redirect logs to stdout  
RUN ln -fs /dev/stdout /var/log/apache2/error.log && \  
ln -fs /dev/stdout /var/log/apache2/other_vhosts_access.log  
  
EXPOSE 80  

