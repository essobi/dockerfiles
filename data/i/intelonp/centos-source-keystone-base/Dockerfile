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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/keystone \--groups kolla keystone \  
&& mkdir -p /var/lib/keystone \  
&& chown -R 42425:42425 /var/lib/keystone  
  
  
  
  
  
RUN yum -y install httpd mod_wsgi python-ldappool && yum clean all  
RUN sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
  
  
  
RUN mkdir -p /keystone-base-source && git clone
git://git.openstack.org/openstack/keystone /keystone-base-source/keystone-base
&& pushd /keystone-base-source/keystone-base && git checkout
78adc33858509cac2f597f7e38a8f5f189ad2495 && popd  
  
RUN ln -s keystone-base-source/* keystone \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /keystone \  
&& mkdir -p /etc/keystone /var/www/cgi-bin/keystone \  
&& cp -r /keystone/etc/* /etc/keystone/ \  
&& cp /var/lib/kolla/venv/bin/keystone-wsgi-admin /var/www/cgi-
bin/keystone/admin \  
&& cp /var/lib/kolla/venv/bin/keystone-wsgi-public /var/www/cgi-
bin/keystone/main \  
&& chown -R keystone: /etc/keystone /var/www/cgi-bin/keystone  
  
  
  
  
RUN chown -R keystone: /var/www/cgi-bin/keystone \  
&& chmod 755 /var/www/cgi-bin/keystone/*  

