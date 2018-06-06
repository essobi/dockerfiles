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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/cinder \--groups kolla cinder \  
&& mkdir -p /var/lib/cinder \  
&& chown -R 42407:42407 /var/lib/cinder  
  
  
  
  
  
  
RUN yum -y install lvm2 qemu-img ceph-common && yum clean all  
  
RUN mkdir -p /cinder-base-source && git clone
git://git.openstack.org/openstack/cinder /cinder-base-source/cinder-base &&
pushd /cinder-base-source/cinder-base && git checkout
20fba8389185c166cd879b797ed3548898601c9a && popd  
  
RUN ln -s cinder-base-source/* cinder \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /cinder \  
&& mkdir -p /etc/cinder \  
&& cp -r /cinder/etc/cinder/* /etc/cinder/ \  
&& chown -R cinder: /etc/cinder \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/cinder/rootwrap.conf  
  
  
  
COPY cinder_sudoers /etc/sudoers.d/kolla_cinder_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_cinder_sudoers \  
&& touch /usr/local/bin/kolla_cinder_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_cinder_extend_start  

