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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/ironic \--groups kolla ironic \  
&& mkdir -p /var/lib/ironic \  
&& chown -R 42422:42422 /var/lib/ironic  
  
  
  
  
RUN mkdir -p /ironic-base-source && git clone
git://git.openstack.org/openstack/ironic /ironic-base-source/ironic-base &&
pushd /ironic-base-source/ironic-base && git checkout
2b92b53da819f32e48e963055fc08b53ead058d9 && popd  
  
RUN ln -s ironic-base-source/* ironic \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /ironic \  
&& mkdir -p /etc/ironic \  
&& cp -r /ironic/etc/ironic/* /etc/ironic/ \  
&& chown -R ironic: /etc/ironic \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/ironic/rootwrap.conf  
  
ADD ironic_sudoers /etc/sudoers.d/kolla_ironic_sudoers  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_ironic_sudoers  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN touch /usr/local/bin/kolla_ironic_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_ironic_extend_start \  
&& chown -R ironic: /etc/ironic  

