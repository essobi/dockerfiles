###  
# vkucukcakar/cron  
# cron Docker image for time-based job scheduling  
# Copyright (c) 2017 Volkan Kucukcakar  
#  
# This file is part of vkucukcakar/cron.  
#  
# vkucukcakar/cron is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 2 of the License, or  
# (at your option) any later version.  
#  
# vkucukcakar/cron is distributed in the hope that it will be useful,  
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
  
# Notes on volumes:  
# Put/mount your executable files into "/etc/periodic/15min/",
"/etc/periodic/hourly/", "/etc/periodic/daily/", "/etc/periodic/weekly/",
"/etc/periodic/monthly/" to schedule with cron.  
# Put/mount your custom crontab file to "/etc/crontabs/root" for arbitrary
scheduling. (Syntax is like Debian's "/etc/cron.d/*" but without username)  
VOLUME [ "/etc/crontabs/", "/etc/periodic/15min/", "/etc/periodic/hourly/",
"/etc/periodic/daily/", "/etc/periodic/weekly/", "/etc/periodic/monthly/" ]  
  
# Note: cron already installed on Alpine  
# Note: Common utilities wget, curl already installed on base image  
# Create cron runit service.  
RUN mkdir -p /etc/service/cron/  
COPY alpine/cron.run /etc/service/cron/run  
RUN chmod 755 /etc/service/cron/run  
  
# Redirect output back to Docker over PID 1  
# You can redirect stdout and stderr back to Docker by using
"/var/log/cron.log" and "/var/log/cron-error.log" (or just "/proc/1/fd/1" and
"/proc/1/fd/2")  
# e.g.: echo "Hello World" >>/var/log/cron.log 2>&1  
# e.g.: echo "Hello World" >>/var/log/cron.log 2>>/var/log/cron-error.log  
RUN ln -sf /proc/1/fd/1 /var/log/cron.log \  
&& ln -sf /proc/1/fd/2 /var/log/cron-error.log  
  
# Setup entrypoint  
COPY alpine/entrypoint.sh /cron/entrypoint.sh  
RUN chmod +x /cron/entrypoint.sh  
ENTRYPOINT ["/sbin/tini", "--", "/runit/entrypoint.sh", "/cron/entrypoint.sh"]  

