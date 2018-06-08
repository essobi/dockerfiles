###  
# vkucukcakar/runit  
# runit Docker image for service supervision and zombie reaping  
# Copyright (c) 2017 Volkan Kucukcakar  
#  
# This file is part of vkucukcakar/runit.  
#  
# vkucukcakar/runit is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 2 of the License, or  
# (at your option) any later version.  
#  
# vkucukcakar/runit is distributed in the hope that it will be useful,  
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
FROM vkucukcakar/base:1.0.3-alpine  
  
LABEL maintainer "Volkan Kucukcakar"  
  
# Install runit for Alpine.  
RUN apk add --update runit \  
&& rm -rf /var/cache/apk/*  
  
# FOR CHILD IMAGES: Create/COPY your own runit service files
(/etc/service/{SERVICENAME}/run) and chmod 755 as follows:  
#RUN mkdir -p /etc/service/example/  
#COPY alpine/example.run /etc/service/example/run  
#RUN chmod 755 /etc/service/example/run  
# See the bundled alpine/example.run runit service file comments for
instructions  
# Set up entrypoint  
COPY alpine/entrypoint.sh /runit/entrypoint.sh  
RUN chmod +x /runit/entrypoint.sh  
ENTRYPOINT ["/sbin/tini", "--", "/runit/entrypoint.sh"]  

