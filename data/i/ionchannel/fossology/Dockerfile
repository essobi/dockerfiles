# Copyright 2015 Selection Pressure, LLC.  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
# http://www.apache.org/licenses/LICENSE-2.0  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
# let's start with ubuntu  
FROM ubuntu:14.04  
# https://github.com/airgap  
# http://airgap.io  
MAINTAINER Kelly Plummer <kellyplummer@mac.com>  
  
# add the fossology repo  
RUN apt-get update  
RUN apt-get install -y apt-transport-https  
RUN echo "deb http://www.fossology.org/releases/2.6.2/Ubuntu/ 14.04 contrib"
>> /etc/apt/sources.list  
  
# update existing packages  
RUN apt-get update  
  
# install postgresql database  
RUN apt-get install -y postgresql  
  
# install fossology from a script, due to the postgresql dependency  
ADD scripts/install_fossology.sh /usr/bin/install_fossology.sh  
RUN install_fossology.sh  
  
# the entrypoint script  
ADD scripts/start_fossology.sh /usr/bin/start_fossology.sh  
  
# setup logs for docker  
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \  
ln -sf /proc/self/fd/1 /var/log/apache2/error.log && \  
ln -sf /proc/self/fd/1 /var/log/apache2/other_vhosts_access.log  
  
# apache is configured for port 80  
EXPOSE 80 443  
# let's go!  
CMD ["/usr/bin/start_fossology.sh"]  

