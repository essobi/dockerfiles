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
  
ENV VERSION="20171222"  
# prepare  
RUN apk update -q && \  
apk upgrade -q && \  
apk add -q \  
git \  
net-snmp-perl \  
perl \  
perl-dbd-mysql \  
perl-json \  
perl-net-dns \  
perl-net-snmp  
  
# install  
RUN mkdir -p /usr/lib/centreon && \  
mkdir -p /var/lib/net-snmp/mib_indexes && \  
cd /usr/lib/centreon && \  
git clone https://github.com/centreon/centreon-plugins.git plugins && \  
cd plugins && \  
git checkout tags/${VERSION} && \  
rm -fr /usr/lib/centreon/plugins/.github && \  
rm -fr /usr/lib/centreon/plugins/changelog && \  
rm -fr /usr/lib/centreon/plugins/contrib && \  
rm -fr /usr/lib/centreon/plugins/docs && \  
rm -fr /usr/lib/centreon/plugins/example && \  
rm -fr /usr/lib/centreon/plugins/LICENSE.txt && \  
rm -fr /usr/lib/centreon/plugins/README.md  
# clean  
RUN apk del -q \  
git && \  
rm -fr /var/cache/apk/*  
  
ENTRYPOINT [ "perl", "/usr/lib/centreon/plugins/centreon_plugins.pl" ]  
  
CMD [ "--version" ]  
# EOF  

