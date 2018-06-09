###  
# vkucukcakar/ip-list-updater  
# ip-list-updater as Docker image. (ip-list-updater: Automatic CDN and bogon
IP list updater for firewall and server configurations)  
# Copyright (c) 2017 Volkan Kucukcakar  
#  
# This file is part of vkucukcakar/ip-list-updater.  
#  
# vkucukcakar/ip-list-updater is free software: you can redistribute it and/or
modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 2 of the License, or  
# (at your option) any later version.  
#  
# vkucukcakar/ip-list-updater is distributed in the hope that it will be
useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
# This copyright notice and license must be retained in all files and
derivative works.  
###  
FROM vkucukcakar/cron:1.0.4-alpine  
  
LABEL maintainer "Volkan Kucukcakar"  
  
# Output Nginx Cloudflare configuration file will be saved to
/configurations/ip-list-updater.lst  
VOLUME [ "/configurations" ]  
  
# Install php7-cli  
RUN apk add --update \  
php7 \  
php7-openssl \  
&& rm -rf /var/cache/apk/*  
  
# Install ip-list-updater  
RUN wget --no-check-certificate https://github.com/vkucukcakar/ip-list-
updater/archive/v1.1.0.tar.gz \  
&& tar -xzvf v1.1.0.tar.gz \  
&& rm v1.1.0.tar.gz \  
&& cp ip-list-updater-1.1.0/ip-list-updater.php /usr/local/bin/ \  
&& rm -rf ip-list-updater-1.1.0  
  
# Copy root crontab to use as template later  
RUN mkdir -p /ip-list-updater/crontabs \  
&& cp /etc/crontabs/root /ip-list-updater/crontabs/  
  
# Setup entrypoint  
COPY files/entrypoint.sh /ip-list-updater/entrypoint.sh  
RUN chmod +x /ip-list-updater/entrypoint.sh  
ENTRYPOINT ["/sbin/tini", "--", "/runit/entrypoint.sh", "/cron/entrypoint.sh"]  
CMD ["/ip-list-updater/entrypoint.sh"]  

