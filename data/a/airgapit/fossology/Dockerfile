# Copyright 2014 AirGap, LLC.  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
# http://www.apache.org/licenses/LICENSE-2.0  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
# let's start with precise pangolin  
FROM ubuntu:12.04  
# https://github.com/airgap  
# http://airgap.io  
MAINTAINER AirGap <engineering@airgap.io>  
  
# add the fossology repo  
RUN echo "deb http://www.fossology.org/releases/2.6.1/Ubuntu/ 12.04 contrib"
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
  
# apache is configured for port 80  
EXPOSE 80  
# let's go!  
ENTRYPOINT ["/usr/bin/start_fossology.sh"]  

