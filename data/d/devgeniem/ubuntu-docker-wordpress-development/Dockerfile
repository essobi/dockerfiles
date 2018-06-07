FROM devgeniem/ubuntu-docker-wordpress:latest  
MAINTAINER Ville Pietarinen - Geniem Oy <ville.pietarinen-nospam@geniem.com>  
  
ENV \  
# Display errors for easier debugging  
PHP_DISPLAY_ERRORS="on" \  
# Directory to store xdebug profiling  
XDEBUG_DIR="/tmp/xdebug" \  
# Use OSX IP address loopback hack:
https://gist.githubusercontent.com/ralphschindler/535dc5916ccbd06f53c1b0ee5a868c93/raw/com.ralphschindler.docker_10254_alias.plist  
# This can be overridden by you  
XDEBUG_REMOTE_HOST="10.254.254.254" \  
XDEBUG_REMOTE_PORT="9000" \  
# You can enable this env to allow profiling your application with xdebug
trigger  
# This is disabled by default because it adds plenty of overhead when it's not
needed  
# Default: disabled  
XDEBUG_ENABLE_PROFILE=0  
# Install xdebug  
RUN \  
# Install package from official repo  
apt-get update \  
&& apt-get install -y php7.1-xdebug \  
# Install mcrypt  
&& apt-get install libmcrypt-dev \  
# Create folder for xdebug profiler  
&& mkdir -p $XDEBUG_DIR \  
# Remove custom error pages because they make debugging harder  
&& echo "# Disabled" > /etc/nginx/error_pages.conf \  
# Cleanup  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
/var/log/apt/*  
  
# Copy our development changes  
COPY etc/ /etc/  

