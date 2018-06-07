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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/heat \--groups kolla heat \  
&& mkdir -p /var/lib/heat \  
&& chown -R 42418:42418 /var/lib/heat  
  
  
  
  
RUN mkdir -p /heat-base-source && git clone
git://git.openstack.org/openstack/heat /heat-base-source/heat-base && pushd
/heat-base-source/heat-base && git checkout
2dd83353c086a8ee3ee8aefb99b06832782d8cab && popd  
  
RUN ln -s heat-base-source/* heat \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /heat \  
&& mkdir -p /etc/heat \  
&& cp -r /heat/etc/heat/* /etc/heat/ \  
&& chown -R heat: /etc/heat  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN touch /usr/local/bin/kolla_heat_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_heat_extend_start  

