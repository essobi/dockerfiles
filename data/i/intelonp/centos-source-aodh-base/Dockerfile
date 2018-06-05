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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/aodh \--groups kolla aodh \  
&& mkdir -p /var/lib/aodh \  
&& chown -R 42402:42402 /var/lib/aodh  
  
  
  
  
  
  
  
RUN yum -y install httpd mod_wsgi python-ldappool && yum clean all  
RUN mkdir -p /var/www/cgi-bin/aodh \  
&& sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
  
RUN mkdir -p /aodh-base-source && git clone
git://git.openstack.org/openstack/aodh /aodh-base-source/aodh-base && pushd
/aodh-base-source/aodh-base && git checkout
2ad5fb78647f8017e9716292495609408e91b10c && popd  
  
  
RUN ln -s aodh-base-source/* aodh \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt pymongo /aodh \  
&& mkdir -p /etc/aodh /var/www/cgi-bin/aodh \  
&& cp -r /aodh/etc/aodh/* /etc/aodh/ \  
&& cp /aodh/aodh/api/app.wsgi /var/www/cgi-bin/aodh \  
&& chown -R aodh: /etc/aodh /var/www/cgi-bin/aodh  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
COPY aodh_sudoers /etc/sudoers.d/kolla_aodh_sudoers  
  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 640 /etc/sudoers.d/kolla_aodh_sudoers \  
&& chmod 755 /var/www/cgi-bin/aodh \  
&& touch /usr/local/bin/kolla_aodh_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_aodh_extend_start  

