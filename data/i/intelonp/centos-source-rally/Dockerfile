# Copyright (c) 2017, Intel Corporation  
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
  
FROM intelonp/centos-source-openstack-base:0018  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/rally \--groups kolla rally \  
&& mkdir -p /var/lib/rally \  
&& chown -R 42440:42440 /var/lib/rally  
  
  
  
  
RUN mkdir -p /rally-source && git clone
git://git.openstack.org/openstack/rally /rally-source/rally && pushd /rally-
source/rally && git checkout 31394284f5cab0d457bf3dde524641de46c7b4e0 && popd  
  
RUN ln -s rally-source/* rally \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /rally \  
&& mkdir -p /etc/rally \  
&& chown -R rally: /etc/rally  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start  
  
  
  
  
USER rally

