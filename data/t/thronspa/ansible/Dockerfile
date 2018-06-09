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
  
FROM ubuntu:bionic  
MAINTAINER THRON Devops <devops@thron.com>  
  
ENV ANSIBLE_VERSION=2.5.4  
  
RUN apt-get update -y \  
&& apt-get install --fix-missing \  
&& DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -y \  
dos2unix \  
gcc \  
libssl-dev \  
libffi-dev \  
python-dev \  
python-pip \  
&& pip install -I ansible==${ANSIBLE_VERSION} \  
&& apt-get -f -y --auto-remove remove gcc \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* \  
&& mkdir -p /etc/ansible \  
&& echo 'localhost' > /etc/ansible/hosts  
  
CMD ["/bin/bash"]  

