###  
# vkucukcakar/ngx-cf-ip  
# ngx-cf-ip as Docker image. (ngx-cf-ip: Cloudflare IP updater for Nginx
ngx_http_realip_module)  
# Copyright (c) 2017 Volkan Kucukcakar  
#  
# This file is part of vkucukcakar/ngx-cf-ip.  
#  
# vkucukcakar/ngx-cf-ip is free software: you can redistribute it and/or
modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 2 of the License, or  
# (at your option) any later version.  
#  
# vkucukcakar/ngx-cf-ip is distributed in the hope that it will be useful,  
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
/configurations/cf.conf  
VOLUME [ "/configurations" ]  
  
# Install php7-cli  
RUN apk add --update \  
php7 \  
php7-openssl \  
&& rm -rf /var/cache/apk/*  
  
# Install ngx-cf-ip  
RUN wget --no-check-certificate https://github.com/vkucukcakar/ngx-cf-
ip/archive/v1.0.2.tar.gz \  
&& tar -xzvf v1.0.2.tar.gz \  
&& rm v1.0.2.tar.gz \  
&& cp ngx-cf-ip-1.0.2/ngx-cf-ip.php /usr/local/bin/ \  
&& rm -rf ngx-cf-ip-1.0.2  
  
# Copy root crontab to use as template later  
RUN mkdir -p /ngx-cf-ip/crontabs \  
&& cp /etc/crontabs/root /ngx-cf-ip/crontabs/  
  
# Setup entrypoint  
COPY files/entrypoint.sh /ngx-cf-ip/entrypoint.sh  
RUN chmod +x /ngx-cf-ip/entrypoint.sh  
ENTRYPOINT ["/sbin/tini", "--", "/runit/entrypoint.sh", "/cron/entrypoint.sh"]  
CMD ["/ngx-cf-ip/entrypoint.sh"]  

