# Copyright 2017 - Present Visual CPU (Dave Kirk)  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
FROM visualcpu/centos-nginx:latest  
MAINTAINER Dave Kirk <dave@visualcpu.com>  
  
# set some default values for the environment variables our nginx container  
# uses  
ENV NGINX_DEFAULT_SITE_ROOT=/workspace/app/public  
ENV NGINX_DEFAULT_APP_SITE_CONF=php-site.conf  
ENV NGINX_DEFAULT_APP_SERVER_CONF=php-fpm.conf  
  
# install php-fpm for nginx  
#  
# - add the epel repo (required for webtatic php)  
# - add the webtatic repo for pre-compiled php packages  
# - install php-fpm  
# - install some useful php modules  
# - ensure the php-fpm process is not running (supervisor will manage it)  
# - copy the php config files for nginx  
RUN set -xe \  
&& rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \  
&& yum install -y \  
php71w-fpm \  
php71w-pear \  
php71w-mysql \  
php71w-bz2 \  
php71w-intl \  
php71w-mbstring \  
php71w-phpdbg \  
php71w-curl \  
php71w-gd \  
php71w-bcmath  
  
COPY etc/php.ini /etc/php.ini  
COPY etc/nginx/php-fpm.conf /etc/nginx/php-fpm.conf  
COPY etc/nginx/php-site.conf /etc/nginx/php-site.conf  
COPY etc/php-fpm.conf /etc/php-fpm.conf  
COPY etc/php-fpm.d/www.conf /etc/php-fpm.d/www.conf  
  
# configure supervisor to run and manage php-fpm  
RUN mkdir -p /var/run/php \  
&& chown nginx:nginx /var/run/php  
COPY etc/supervisor/conf.d/php-fpm.conf /etc/supervisor/conf.d/php-fpm.conf  
  
# finally, add our startup scripts  
COPY usr/local/container-startup/20-php-fpm-logs.sh /usr/local/container-
startup/20-php-fpm-logs.sh  
COPY usr/local/container-startup/20-php-fpm-sessions.sh /usr/local/container-
startup/20-php-fpm-sessions.sh  
RUN chmod 755 /usr/local/container-startup/20-php-fpm-logs.sh \  
&& chmod 755 /usr/local/container-startup/20-php-fpm-sessions.sh  

