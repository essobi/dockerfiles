###  
# vkucukcakar/rsyslog  
# rsyslog and logrotate Docker image with automatic configuration file
creation and export  
# Copyright (c) 2017 Volkan Kucukcakar  
#  
# This file is part of vkucukcakar/rsyslog.  
#  
# vkucukcakar/rsyslog is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 2 of the License, or  
# (at your option) any later version.  
#  
# vkucukcakar/rsyslog is distributed in the hope that it will be useful,  
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
FROM vkucukcakar/runit:1.0.4-alpine  
  
LABEL maintainer "Volkan Kucukcakar"  
  
EXPOSE 5514 5514/udp  
  
VOLUME [ "/var/log", "/configurations" ]  
  
# Install cron, rsyslog, logrotate, netcat (for the nc command that will be
used for healthcheck later), gettext (for envsubst command that will be
required for entrypoint later)  
RUN apk add --update \  
rsyslog \  
logrotate \  
&& rm -rf /var/cache/apk/*  
  
# Note: cron, netcat, gettext already installed on base image  
# Clear default cron directories, delete cron files except "logrotate" and
".placeholder" files using find command.  
# rm -f also suspend errors even the directory is not found.  
RUN find /etc/periodic/daily -type f ! -name 'logrotate' -delete  
  
# Create logrotate cron and rsyslog runit services.  
RUN mkdir -p /etc/service/cron/ \  
&& mkdir -p /etc/service/rsyslog/  
COPY alpine/logrotate-cron.run /etc/service/cron/run  
COPY common/rsyslog.run /etc/service/rsyslog/run  
RUN chmod 755 /etc/service/cron/run \  
&& chmod 755 /etc/service/rsyslog/run  
  
# Disable default configuration file(s)  
RUN mv /etc/rsyslog.conf /etc/rsyslog.conf.bak \  
&& mv /etc/logrotate.conf /etc/logrotate.conf.bak  
  
# Remove default rsyslog and logrotate configuration files  
RUN rm /etc/logrotate.d/*  
#&& rm /etc/rsyslog.d/*; exit 0  
# Create "/var/spool/rsyslog" directory (referred in the common rsyslog.conf)
for Alpine  
RUN mkdir -p /var/spool/rsyslog  
  
# Create "/etc/rsyslog.d" directory for Alpine  
RUN mkdir -p /etc/rsyslog.d  
  
# Copy template configuration files  
COPY templates /templates  
  
# Healthcheck with netcat  
HEALTHCHECK \--interval=10s --timeout=10s --retries=3 CMD nc -z localhost 5514
|| exit 1  
  
# Setup entrypoint  
COPY common/entrypoint.sh /rsyslog/entrypoint.sh  
RUN chmod +x /rsyslog/entrypoint.sh  
ENTRYPOINT ["/sbin/tini", "--", "/runit/entrypoint.sh",
"/rsyslog/entrypoint.sh"]  

