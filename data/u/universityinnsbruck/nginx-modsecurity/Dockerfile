FROM phusion/baseimage:latest  
MAINTAINER Gregor Schwab <gregor.schwab@uibk.ac.at>  
  
# http://myshell.co.uk/index.php/adjusting-child-processes-for-php-fpm-nginx/  
# http://jeremymarc.github.io/2013/04/22/nginx-and-php-fpm-for-performance/  
# https://serversforhackers.com/compiling-third-party-modules-into-nginx  
# http://xybu.me/setting-up-a-ubuntu-server/  
# Regenerate SSH host keys and allow ssh.  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Set Timezone  
RUN echo "Europe/Berlin" | tee /etc/timezone  
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Berlin
/etc/localtime  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
# Update Package List  
RUN apt-get update  
  
# Installing the 'apt-utils' package gets rid of the 'debconf: delaying
package configuration, since apt-utils is not installed'  
# error message when installing any other package with the apt-get package
manager.  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
apt-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Some PPAs  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y vim
curl wget build-essential software-properties-common git sudo  
RUN DEBIAN_FRONTEND=noninteractive apt-add-repository -y ppa:nginx/development  
  
#------------------------------  
# Install Nginx  
#------------------------------  
# Create work directories  
RUN mkdir /opt/nginx \  
&& mkdir /opt/nginx/build \  
&& mkdir /opt/nginx/modules  
  
# Uncomment deb-src  
RUN sed -i "s|# deb-src http://ppa.launchpad.net/nginx/development/ubuntu
xenial main|deb-src http://ppa.launchpad.net/nginx/development/ubuntu xenial
main|" /etc/apt/sources.list.d/nginx-ubuntu-development-xenial.list  
  
# Nginx compile req packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
--allow-downgrades --allow-remove-essential --allow-change-held-packages dpkg-
dev nginx-common  
  
# Add ModSecurity Module  
# https://github.com/SpiderLabs/ModSecurity/wiki/Reference-
Manual#Installation_for_NGINX  
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-downgrades
--allow-remove-essential --allow-change-held-packages libxml2 libxml2-dev
libxml2-utils libaprutil1 libaprutil1-dev \  
libpcre-ocaml-dev autoconf make automake libtool \  
libpcre3 libpcre3-dev libpcrecpp0v5 libssl-dev zlib1g-dev apache2-dev  
WORKDIR /opt/nginx/modules  
RUN git clone https://github.com/SpiderLabs/ModSecurity.git mod_security  
WORKDIR mod_security  
RUN ./autogen.sh  
RUN ./configure --enable-standalone-module  
RUN make  
  
# Set work directory  
WORKDIR /opt/nginx/build  
  
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install debian-keyring  
# First of all, import the nginx key  
# Then export the key to your local trustedkeys to make it trusted  
RUN sudo gpg --keyserver keyserver.ubuntu.com --recv-keys F569EF55 && gpg
--no-default-keyring -a --export F569EF55 | gpg --no-default-keyring --keyring
~/.gnupg/trustedkeys.gpg --import -  
# Get Nginx (ppa:nginx/stable) source files  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get source nginx  
  
# Install the build dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get build-dep -y --allow-downgrades
--allow-remove-essential --allow-change-held-packages nginx  
  
# Add Modules  
RUN sed -i '/ngx_http_substitutions_filter_module/ a\\\t\t\t--add-
module=\/opt\/nginx\/modules\/mod_security\/nginx\/modsecurity'
/opt/nginx/build/nginx-*/debian/rules  
RUN sed -i
's/ngx_http_substitutions_filter_module/ngx_http_substitutions_filter_module
\\\/' /opt/nginx/build/nginx-*/debian/rules  
  
# build the package  
RUN cd nginx-* && pwd && dpkg-buildpackage -b -uc -us  
  
# Install nginx  
RUN apt-get update && dpkg --install libnginx-mod-*.deb && dpkg --install
nginx-extras_*_amd64.deb  
  
#------------------------------  
# Configure Nginx  
#------------------------------  
# Add ModSecurity Recommended Base Configuration  
WORKDIR /opt/nginx/modules/mod_security  
RUN cp modsecurity.conf-recommended /etc/nginx/modsecurity.conf  
RUN cp unicode.mapping /etc/nginx/  
#  
# Add OWASP Base Configuration  
RUN wget https://github.com/SpiderLabs/owasp-modsecurity-crs/tarball/master -O
owasp.tar.gz && tar -zxvf owasp.tar.gz && rm owasp.tar.gz  
RUN cd SpiderLabs-owasp-modsecurity-crs-* && cat
modsecurity_crs_10_setup.conf.example >> /etc/nginx/modsecurity.conf  
RUN cd SpiderLabs-owasp-modsecurity-crs-*/base_rules && cat *.conf >>
/etc/nginx/modsecurity.conf  
RUN cd SpiderLabs-owasp-modsecurity-crs-*/base_rules && cp *.data /etc/nginx  
  
# Brute Force Attacks with Nginx limit Req Module  
# https://rtcamp.com/tutorials/nginx/block-wp-login-php-bruteforce-attack/  
# Simulate Attack: ab -n 100 -c 10 example.com/index.php  
RUN sed -i '/server_tokens off;/ a\limit_req_zone $binary_remote_addr
zone=one:10m rate=10r\/s;' /etc/nginx/nginx.conf  
RUN sed -i '/limit_req_zone $binary_remote_addr zone=one:10m rate=1r\/s;/
a\limit_req_status 444;' /etc/nginx/nginx.conf  
  
# Create default app directory  
RUN rm -rf /var/www  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Shell script must run the daemon without letting it daemonize/fork it  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Hide nginx server tokens and version number  
RUN sed -i "s/# server_tokens off;/server_tokens off;/" /etc/nginx/nginx.conf  
  
# Gzip setup  
RUN sed -i "/gzip_disable "msie6";/ a\gzip_min_length 10240;"
/etc/init.d/nginx  
RUN sed -i "s/# gzip_vary on;/gzip_vary on;/" /etc/nginx/nginx.conf  
RUN sed -i "s/# gzip_proxied any;/gzip_proxied expired no-cache no-store
private auth;/" /etc/nginx/nginx.conf  
RUN sed -i "s/# gzip_types/gzip_types/" /etc/nginx/nginx.conf  
  
#------------------------------  
# Custom Scripts  
#------------------------------  
RUN mkdir /opt/build-scripts  
RUN chmod +x /opt/build-scripts  
COPY build/config.sh /opt/build-scripts/config.sh  
  
#------------------------------  
# Startup Scripts  
#------------------------------  
# create script directory  
RUN mkdir -p /etc/my_init.d  
  
# add scripts  
ADD build/envars.sh /etc/my_init.d/01_envars.sh  
  
# update script permissions  
RUN chmod +x /etc/my_init.d/*  
  
# build the daemon  
RUN mkdir /etc/service/nginx  
ADD build/nginx/nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
#------------------------------  
# Finish and Cleanup  
#------------------------------  
EXPOSE 80 22  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/opt/nginx/*  
  
#make audit concurrent  
RUN mkdir -p /opt/modsecurity/var/audit/  
RUN chown -R www-data:www-data /opt/modsecurity/var/audit/  
RUN sed -i "s/SecAuditLogType Serial/SecAuditLogType Concurrent/"
/etc/nginx/modsecurity.conf  
RUN sed -i "s/SecAuditLog\\(\s.*\\)/# SecAuditLog\1/"
/etc/nginx/modsecurity.conf  
RUN sed -i "/# SecAuditLog\s.*/a SecAuditLogStorageDir
\/opt\/modsecurity\/var\/audit/" /etc/nginx/modsecurity.conf  
  

