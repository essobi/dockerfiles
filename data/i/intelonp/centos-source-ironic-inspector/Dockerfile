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
  
FROM intelonp/centos-source-ironic-base:0018  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
  
RUN mkdir -p /ironic-inspector-source && git clone
git://git.openstack.org/openstack/ironic-inspector /ironic-inspector-
source/ironic-inspector && pushd /ironic-inspector-source/ironic-inspector &&
git checkout 7d0806b664f43e1fbaf70a6ee70c06a79901e676 && popd  
  
RUN ln -s ironic-inspector-source/* ironic-inspector \  
&& mv /etc/ironic /etc/ironic-inspector \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /ironic-inspector \  
&& cp /ironic-inspector/rootwrap.conf /etc/ironic-inspector/ \  
&& cp -r /ironic-inspector/rootwrap.d/ /etc/ironic-inspector/ \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/ironic-inspector/rootwrap.conf  
  
  
  
COPY ironic_sudoers /etc/sudoers.d/kolla_ironic_inspector_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_ironic_extend_start  
  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_ironic_inspector_sudoers \  
&& chmod 755 /usr/local/bin/kolla_ironic_extend_start  
  
  
  
  
USER ironic

