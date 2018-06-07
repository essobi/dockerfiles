# Dockerized wikipedia-dump-tools  
#  
# URL: https://github.com/William-Yeh/docker-wikipedia-dump-tools  
#  
# Reference: https://github.com/sunlightlabs/wikipedia-dump-tools  
#  
# Version 0.1  
#  
#----------  
# Dockerized wikipedia-dump-tools  
# Copyright (C) 2014 William Yeh <william.pjyeh@gmail.com>  
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
#----------  
# pull base image  
FROM williamyeh/python2  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
ENV TARBALL https://github.com/sunlightlabs/wikipedia-dump-
tools/archive/master.zip  
  
  
RUN apt-get update  
  
# Install curl & helper tools  
RUN apt-get install -y -q --no-install-recommends curl unzip  
  
RUN mkdir -p /opt/wikipedia-dump-tools  
  
# download & compile  
RUN \  
cd /tmp && \  
curl -OL $TARBALL && \  
unzip *.zip && \  
mv wikipedia-dump-tools-master/* /opt/wikipedia-dump-tools/ && \  
cd /opt/wikipedia-dump-tools && \  
sed -i -e 's/^import sys$/import
sys\nreload(sys)\nsys.setdefaultencoding("utf8")\n/'
wikitools/pageprocessor.py && \  
apt-get install --no-install-recommends -y -q libxml2-dev libxslt1-dev
zlib1g-dev && \  
pip install lxml functional inflect && \  
python setup.py install  
  
# Uninstall curl & help tools  
RUN apt-get remove -y --auto-remove curl unzip && \  
apt-get clean  
  
# clean up  
RUN rm -rf /tmp/*  
  
#----------------------------#  
# configure  
VOLUME [ "/data" ]  
WORKDIR /data  
  
# for convenience  
ENV TOOLS_PATH /opt/wikipedia-dump-tools  
ENV PATH $TOOLS_PATH:$PATH  
COPY usage.sh /opt/wikipedia-dump-tools/  
COPY help /opt/wikipedia-dump-tools/  
COPY extract-text /opt/wikipedia-dump-tools/  
RUN date '+%Y-%m-%dT%H:%M:%S%:z' > /var/log/DOCKER_BUILD_TIME  
  
# Define default command.  
CMD ["usage.sh"]  
  

