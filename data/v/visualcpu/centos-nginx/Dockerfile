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
FROM visualcpu/centos:7  
MAINTAINER Dave Kirk <dave@visualcpu.com>  
  
# install nginx  
#  
# - configure the yum repo so we can get the latest version of nginx  
# - install the package(s)  
COPY etc/yum.repos.d/nginx.repo /etc/yum.repos.d/nginx.repo  
RUN set -xe \  
&& yum install -y nginx  
  
# configure nginx  
#  
# - copy the global config file  
# - copy across static site configuration (index files, image rules, robot.txt
rules, etc)  
# - remove the default site  
# - create the sites-available and sites-enabled directories (I like how
Ubuntu do this)  
# - add an empty file to load if no custom config supplied  
# - copy across the default site config file  
# - enable the default site  
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY etc/nginx/drop.conf /etc/nginx/drop.conf  
COPY etc/nginx/images.conf /etc/nginx/images.conf  
COPY etc/nginx/static-site.conf /etc/nginx/static-site.conf  
  
RUN rm -f /etc/nginx/default.conf \  
&& mkdir -p -m 0755 /etc/nginx/sites-available \  
&& mkdir -p -m 0755 /etc/nginx/sites-enabled \  
&& touch /etc/nginx/empty.conf  
  
COPY etc/nginx/sites-available/default.conf /etc/nginx/sites-
available/default.conf  
RUN ln -sf /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# configure supervisor to manage nginx  
COPY etc/supervisor/conf.d/nginx.conf /etc/supervisor/conf.d/nginx.conf  
  
# image start up  
#  
# copy across the scripts we would like to execute when our container start  
#  
# - logs  
# - set environment variables used in nginx config files  
COPY usr/local/container-startup/50-nginx-logs.sh /usr/local/container-
startup/50-nginx-logs.sh  
COPY usr/local/container-startup/55-nginx-env-vars.sh /usr/local/container-
startup/55-nginx-env-vars.sh  
RUN chmod 0755 /usr/local/container-startup/50-nginx-logs.sh \  
&& chmod 0755 /usr/local/container-startup/55-nginx-env-vars.sh  

