#  
# This file is part of VirtualBox.  
#  
# VirtualBox is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# VirtualBox is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with VirtualBox. If not, see <http://www.gnu.org/licenses/>.  
FROM ubuntu:16.04  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
COPY run.sh /opt/docker/  
RUN ["/bin/sh", "/opt/docker/run.sh"]  
ENTRYPOINT ["VirtualBox"]  
CMD []  

