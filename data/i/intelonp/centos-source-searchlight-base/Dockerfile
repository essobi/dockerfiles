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
  
FROM intelonp/centos-source-openstack-base:0015  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/searchlight \--groups kolla searchlight \  
&& mkdir -p /var/lib/searchlight \  
&& chown -R 42442:42442 /var/lib/searchlight  
  
  
  
  
RUN mkdir -p /searchlight-base-source && git clone
https://github.com/openstack/searchlight /searchlight-base-source/searchlight-
base && pushd /searchlight-base-source/searchlight-base && git checkout
48771e29f7b5b6d1a4600aca69e2cd4be8d4b58b && popd  
  
RUN ln -s searchlight-base-source/* searchlight \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /searchlight \  
&& mkdir -p /etc/searchlight \  
&& cp -r /searchlight/etc/* /etc/searchlight \  
&& chown -R searchlight: /etc/searchlight  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN touch /usr/local/bin/kolla_searchlight_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_searchlight_extend_start  

