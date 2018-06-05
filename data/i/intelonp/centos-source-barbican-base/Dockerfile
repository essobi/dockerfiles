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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/barbican \--groups kolla barbican \  
&& mkdir -p /var/lib/barbican \  
&& chown -R 42403:42403 /var/lib/barbican  
  
  
  
  
  
  
  
RUN yum -y install uwsgi-plugin-python && yum clean all  
  
RUN mkdir -p /barbican-base-source && git clone
git://git.openstack.org/openstack/barbican /barbican-base-source/barbican-base
&& pushd /barbican-base-source/barbican-base && git checkout
d0ebc6c321a840c2d3c8ae5a682d721da7b4a239 && popd  
  
RUN ln -s barbican-base-source/* barbican \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt pastedeploy uwsgi MySQL-python python-
barbicanclient /barbican \  
&& mkdir -p /etc/barbican \  
&& cp -r /barbican/etc/barbican/* /etc/barbican/ \  
&& chown -R barbican: /etc/barbican  
  
  
  
COPY barbican_sudoers /etc/sudoers.d/kolla_barbican_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 640 /etc/sudoers.d/kolla_barbican_sudoers \  
&& touch /usr/local/bin/kolla_barbican_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_barbican_extend_start  

