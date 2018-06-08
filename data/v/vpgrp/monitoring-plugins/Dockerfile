# Copyright (c) 2018 Vente-Privée  
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
FROM vpgrp/alpine:latest  
  
ENV VERSION="2.2"  
# prepare  
RUN apk update -q && \  
apk upgrade -q && \  
apk add -q \  
autoconf \  
automake \  
gcc \  
git \  
libc-dev \  
linux-headers \  
make  
  
# install  
RUN mkdir -p /usr/lib/nagios && \  
mkdir -p /usr/src && \  
cd /usr/src && \  
git clone https://github.com/monitoring-plugins/monitoring-plugins.git && \  
cd monitoring-plugins && \  
git checkout tags/v${VERSION} && \  
sh tools/setup && \  
sh configure \  
\--prefix='/usr' \  
\--libexecdir='/usr/lib/nagios/plugins' \  
\--disable-maintainer-mode && \  
make && \  
make install  
  
# clean  
RUN apk del -q \  
autoconf \  
automake \  
gcc \  
git \  
libc-dev \  
linux-headers \  
make && \  
rm -fr /usr/src/monitoring-plugins && \  
rm -fr /var/cache/apk/*  
# EOF  

