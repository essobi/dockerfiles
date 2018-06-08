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
FROM intelonp/centos-source-neutron-base:0018  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
RUN yum -y install haproxy net-tools && yum clean all  
  
RUN mkdir -p /neutron-lbaas-agent-source && git clone
git://git.openstack.org/openstack/neutron-lbaas /neutron-lbaas-agent-
source/neutron-lbaas-agent && pushd /neutron-lbaas-agent-source/neutron-lbaas-
agent && git checkout 4876dcccbf8571dda461edaca442f2ccc412cd3b && popd  
  
RUN ln -s neutron-lbaas-agent-source/* neutron_lbaas \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /neutron_lbaas \  
&& cp /neutron_lbaas/etc/neutron/rootwrap.d/* /etc/neutron/rootwrap.d \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/neutron/rootwrap.conf  
  
COPY extend_start.sh /usr/local/bin/kolla_neutron_extend_start  
RUN chmod 755 /usr/local/bin/kolla_neutron_extend_start  
  
USER neutron

