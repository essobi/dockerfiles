#  
# Installs WordPress with wp-cli (wp.cli.org) installed and support for mysql,
ssh, less, wp-cli, vim-tiny, rsync  
# Docker Hub: https://registry.hub.docker.com/u/tmuka/wpcua/  
# Github Repo: https://github.com/conetix/docker-wordpress-wp-cli  
# https://github.com/tmuka/docker-cuaws-wpcua.git  
  
FROM wordpress:latest  
MAINTAINER Tony Muka <tmuka@cuanswers.com>  
  
# Add sudo in order to run wp-cli as the www-data user  
RUN apt-get update && apt-get install -y --no-install-recommends \  
sudo \  
less \  
mysql-client \  
openssh-client \  
vim-tiny \  
rsync \  
libldap2-dev \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap  
  
  
# Add WP-CLI  
RUN curl -o /bin/wp-cli.phar https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar  
COPY wp-su.sh /bin/wp  
RUN chmod +x /bin/wp-cli.phar /bin/wp  
  
# Cleanup  
#RUN apt-get clean  
#RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

