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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/gnocchi --groups kolla gnocchi \  
&& mkdir -p /var/lib/gnocchi \  
&& chown -R 42416:42416 /var/lib/gnocchi  
  
RUN yum -y install httpd mod_wsgi python-ldappool python-rados && yum clean
all  
RUN mkdir -p /var/www/cgi-bin/gnocchi \  
&& sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
RUN mkdir -p /gnocchi-base-source && git clone
git://git.openstack.org/openstack/gnocchi /gnocchi-base-source/gnocchi-base &&
pushd /gnocchi-base-source/gnocchi-base && git checkout
2814b6f40d43d4da41377724b5b9dad15e096350 && popd  
  
RUN ln -s gnocchi-base-source/* gnocchi \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /gnocchi[keystone,mysql,file,ceph] \  
&& mkdir -p /etc/gnocchi \  
&& chown -R gnocchi: /etc/gnocchi  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
COPY gnocchi_sudoers /etc/sudoers.d/kolla_gnocchi_sudoers  
  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 640 /etc/sudoers.d/kolla_gnocchi_sudoers \  
&& touch /usr/local/bin/kolla_gnocchi_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_gnocchi_extend_start  

