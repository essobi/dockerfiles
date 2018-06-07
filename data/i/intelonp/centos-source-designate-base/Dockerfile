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
  
  
  
  
  
  
  
  
RUN usermod \--append \--home /var/lib/designate \--groups kolla designate \  
&& mkdir -p /var/lib/designate \  
&& chown -R 42411:42411 /var/lib/designate  
  
  
  
  
RUN mkdir -p /designate-base-source && git clone
git://git.openstack.org/openstack/designate /designate-base-source/designate-
base && pushd /designate-base-source/designate-base && git checkout
b029ac9934720fde7610b4c955c002fc70f5ae42 && popd  
  
RUN ln -s designate-base-source/* designate \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /designate \  
&& mkdir -p /etc/designate \  
&& cp -r /designate/etc/designate/* /etc/designate/ \  
&& mv /etc/designate/rootwrap.conf.sample /etc/designate/rootwrap.conf \  
&& chown -R designate: /etc/designate \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/designate/rootwrap.conf  
  
  
COPY designate_sudoers /etc/sudoers.d/kolla_designate_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 640 /etc/sudoers.d/kolla_designate_sudoers \  
&& touch /usr/local/bin/kolla_designate_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_designate_extend_start  

