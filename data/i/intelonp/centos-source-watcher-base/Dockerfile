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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/watcher \--groups kolla watcher \  
&& mkdir -p /var/lib/watcher \  
&& chown -R 42451:42451 /var/lib/watcher  
  
  
  
  
RUN mkdir -p /watcher-base-source && git clone
git://git.openstack.org/openstack/watcher /watcher-base-source/watcher-base &&
pushd /watcher-base-source/watcher-base && git checkout
1caf89686c7f13e8164dbbd6bd8c09b9ee66f9c4 && popd  
  
RUN ln -s watcher-base-source/* watcher \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /watcher \  
&& mkdir -p /etc/watcher \  
&& cp -r /watcher/etc/watcher/* /etc/watcher/ \  
&& chown -R watcher: /etc/watcher  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN touch /usr/local/bin/kolla_watcher_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_watcher_extend_start  

