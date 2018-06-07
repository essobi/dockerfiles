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
  
  
  
  
  
  
  
  
RUN usermod --append --home /var/lib/horizon \--groups kolla horizon \  
&& mkdir -p /var/lib/horizon \  
&& chown -R 42420:42420 /var/lib/horizon  
  
  
  
  
  
  
  
RUN yum -y install httpd mod_wsgi gettext && yum clean all  
  
  
RUN sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
  
  
  
RUN mkdir -p /horizon-source && git clone
git://git.openstack.org/openstack/horizon /horizon-source/horizon && pushd
/horizon-source/horizon && git checkout
d011d85926c21f7fa228dad0b2847db66928c422 && popd  
  
RUN mkdir -p /plugins && git clone git://git.openstack.org/openstack/neutron-
lbaas-dashboard /plugins/horizon-plugin-neutron-lbaas-dashboard && pushd
/plugins/horizon-plugin-neutron-lbaas-dashboard && git checkout
a2e63f8488be5687722708489e7f63e5d5c487a0 && popd  
RUN mkdir -p /plugins && git clone https://github.com/openstack/magnum-ui
/plugins/horizon-plugin-magnum-dashboard && pushd /plugins/horizon-plugin-
magnum-dashboard && git checkout db3bfff643ceb9353c7c0cafdd4e15e0fcf01fb1 &&
popd  
RUN mkdir -p /plugins && git clone https://github.com/openstack/trove-
dashboard /plugins/horizon-plugin-trove-dashboard && pushd /plugins/horizon-
plugin-trove-dashboard && git checkout
27e3dd2b9648bf32346e5bedbdd42de934e4d0f9 && popd  
RUN mkdir -p /plugins && git clone https://github.com/openstack/murano-
dashboard /plugins/horizon-plugin-murano-dashboard && pushd /plugins/horizon-
plugin-murano-dashboard && git checkout
cfe3f13c61214effe48f060de60754446a0fcf4d && popd  
  
RUN ln -s horizon-source/* horizon \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /horizon \  
&& mkdir -p /etc/openstack-dashboard \  
&& ln -s /etc/openstack-dashboard/local_settings
/var/lib/kolla/venv/lib/python2.7/site-
packages/openstack_dashboard/local/local_settings.py \  
&& cp -r /horizon/openstack_dashboard/conf/* /etc/openstack-dashboard/ \  
&& cp /horizon/openstack_dashboard/local/local_settings.py.example
/etc/openstack-dashboard/local_settings \  
&& cp /horizon/manage.py /var/lib/kolla/venv/bin/manage.py \  
&& if [ "$(ls /plugins)" ]; then \  
pip --no-cache-dir install --upgrade -c requirements/upper-constraints.txt
/plugins/*; \  
fi \  
&& (cd /var/lib/kolla/venv/lib/python2.7/site-packages/horizon &&
/var/lib/kolla/venv/bin/python /var/lib/kolla/venv/bin/manage.py
compilemessages) \  
&& (cd /var/lib/kolla/venv/lib/python2.7/site-packages/openstack_dashboard &&
/var/lib/kolla/venv/bin/python /var/lib/kolla/venv/bin/manage.py
compilemessages) \  
&& chown -R horizon: /etc/openstack-dashboard
/var/lib/kolla/venv/lib/python2.7/site-packages/static  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start  

