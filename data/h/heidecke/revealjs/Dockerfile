# vim:set ft=dockerfile:  
# Copyright 2015 Solinea, Inc.  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
# Adapted from https://github.com/jamtur01/docker-
presentation/blob/master/Dockerfile  
FROM debian:jessie  
  
MAINTAINER Luke Heidecke <luke@solinea.com>  
  
# Instal pre-requisites  
RUN pkgList=' \  
bzip2 \  
git \  
nodejs \  
npm \  
' \  
&& apt-get update -y -q -q \  
&& apt-get install --no-install-recommends -y -q $pkgList \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
WORKDIR /opt  
  
# Install reveal.js  
RUN git clone https://github.com/hakimel/reveal.js.git presentation \  
&& cd /opt/presentation \  
&& npm install -g grunt-cli \  
&& npm install \  
&& sed -i "s/port: port/port: port,\n\t\t\t\t\thostname: \'\'/g" Gruntfile.js  
  
WORKDIR /opt/presentation  
  
EXPOSE 8000  
CMD [ "grunt", "serve" ]

