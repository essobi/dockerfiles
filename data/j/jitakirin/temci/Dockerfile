# docker-temci  
# Copyright (C) 2016 jitakirin  
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
FROM python:3  
MAINTAINER jitakirin <jitakirin@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends time \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip3 install temci  
  
ADD docker-init.sh temci-run.sh /usr/local/bin/  
  
WORKDIR /src  
EXPOSE 8000  
ENTRYPOINT ["/usr/local/bin/docker-init.sh"]  

