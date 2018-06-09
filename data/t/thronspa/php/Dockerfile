# Copyright (C) 2016 THRON S.p.A.  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
  
FROM ubuntu:trusty  
MAINTAINER THRON Devops <devops@thron.com>  
  
ENV TERM=xterm \  
PATH=${PATH}:/usr/lib/jvm/default/bin \  
AWSCLI_VERSION="1.11.63" \  
J2CLI_VERSION="0.3.1-0"  
  
RUN apt-get update \  
&& apt-get install -y \  
cifs-utils \  
wget \  
nano \  
iputils-ping \  
jq \  
net-tools \  
nginx \  
openssh-server \  
php5-fpm \  
php5-dev \  
php5-curl \  
php5-xdebug \  
php-pear \  
php5-ldap \  
php5-mcrypt \  
php5-gd \  
python-pip \  
supervisor \  
&& pip install -I \  
awscli==${AWSCLI_VERSION} \  
j2cli==${J2CLI_VERSION} \  
&& echo "[INFO] Nginx conf" \  
&& mkdir -p /var/www/ \  
&& echo "[INFO] Cleaning container" \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get autoremove -y --purge \  
python-dev  
  
COPY files/ /  
  
RUN chmod 755 /etc/docker/start.sh \  
&& chmod 644 /etc/supervisor/supervisord.conf \  
&& chmod 644 /etc/nginx/nginx.conf \  
&& chmod 644 /etc/php5/fpm/php.ini \  
&& chmod 644 /etc/php5/fpm/php-fpm.conf \  
&& chmod 644 /etc/php5/fpm/pool.d/www.conf \  
&& chmod 644 /etc/php5/mods-available/http.ini  
  
  
  
ENTRYPOINT ["/etc/docker/start.sh"]  

