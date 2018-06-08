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
  
  
  
  
  
  
  
  
RUN usermod \--append \--home /var/lib/neutron \--groups kolla neutron \  
&& mkdir -p /var/lib/neutron \  
&& chown -R 42435:42435 /var/lib/neutron  
  
  
  
  
  
  
  
  
  
  
  
RUN yum -y install conntrack-tools dnsmasq dnsmasq-utils ipset keepalived
python-openvswitch uuid && yum clean all  
  
RUN mkdir -p /neutron-base-source && git clone
git://git.openstack.org/openstack/neutron /neutron-base-source/neutron-base &&
pushd /neutron-base-source/neutron-base && git checkout
9886bdaf1f1654cd88961615c3cdb89e6d05e82e && popd  
  
RUN mkdir -p /plugins && git clone git://git.openstack.org/openstack/neutron-
lbaas-dashboard /plugins/horizon-plugin-neutron-lbaas-dashboard && pushd
/plugins/horizon-plugin-neutron-lbaas-dashboard && git checkout
a2e63f8488be5687722708489e7f63e5d5c487a0 && popd  
RUN mkdir -p /plugins && git clone https://github.com/openstack/neutron-lbaas
/plugins/neutron-lbaas && pushd /plugins/neutron-lbaas && git checkout
924eac815439eedc1225e655811706271a300f74 && popd  
  
RUN ln -s neutron-base-source/* neutron \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /neutron \  
&& mkdir -p /etc/neutron /usr/share/neutron \  
&& cp -r /neutron/etc/* /etc/neutron/ \  
&& cp -r /neutron/etc/neutron/* /etc/neutron/ \  
&& cp /neutron/etc/api-paste.ini /usr/share/neutron \  
&& mv /etc/neutron/neutron/ /etc/neutron/plugins/ \  
&& chown -R neutron: /etc/neutron /usr/share/neutron \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/neutron/rootwrap.conf \  
&& if [ "$(ls /plugins)" ]; then \  
pip \--no-cache-dir install \--upgrade -c requirements/upper-constraints.txt
/plugins/*; \  
fi  
  
  
  
COPY neutron_sudoers /etc/sudoers.d/kolla_neutron_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_neutron_sudoers \  
&& touch /usr/local/bin/kolla_neutron_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_neutron_extend_start

