#  
# <meta:header>  
# <meta:licence>  
# Copyright (c) 2015, MetaGrid (http://www.metagrid.co.uk/)  
# Based on original from FireThorn project (http://www.roe.ac.uk/)  
#  
# This information is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This information is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
# </meta:licence>  
# </meta:header>  
#  
#  
# Based on current Debian.  
FROM debian:wheezy  
MAINTAINER Dave Morris <docker-admin@metagrid.co.uk>  
  
#  
# Disable interactive install.  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Install sudo.  
RUN apt-get update \  
&& apt-get -y install \  
sudo  
  
#  
# Install the notroot script.  
COPY notroot.sh /notroot.sh  
RUN chmod a+x,a-w /notroot.sh  
  
#  
# Set notroot as the entrypoint.  
ENTRYPOINT ["/notroot.sh"]  
  

