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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/congress \--groups kolla congress \  
&& mkdir -p /var/lib/congress \  
&& chown -R 42410:42410 /var/lib/congress  
  
  
  
  
RUN mkdir -p /congress-base-source && git clone
git://git.openstack.org/openstack/congress /congress-base-source/congress-base
&& pushd /congress-base-source/congress-base && git checkout
d635bad1ae10d84e8542916d18af573d4b1d1280 && popd  
  
RUN ln -s congress-base-source/* congress \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /congress \  
&& mkdir -p /etc/congress \  
&& cp -r /congress/etc/* /etc/congress/ \  
&& chown -R congress: /etc/congress  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN touch /usr/local/bin/kolla_congress_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_congress_extend_start  

