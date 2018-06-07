FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
  
RUN yum -y install httpd mod_wsgi gettext && yum clean all  
  
  
RUN sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
  
  
  
RUN mkdir -p /horizon-source && git clone
git://git.openstack.org/openstack/horizon /horizon-source/horizon && pushd
/horizon-source/horizon && git checkout
f9b676aba63a55e61301dd4e4a1f58667b399e35 && popd  
  
ADD plugins-archive /  
RUN ln -s horizon-source/* horizon \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /horizon \  
&& useradd --user-group horizon \  
&& mkdir -p /etc/openstack-dashboard /home/horizon \  
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
ln -s `find /plugins -name 'neutron-lbaas-dashboard-*' -type
d`/neutron_lbaas_dashboard/enabled/_1481_project_ng_loadbalancersv2_panel.py \  
/var/lib/kolla/venv/lib/python2.7/site-
packages/openstack_dashboard/enabled/_1481_project_ng_loadbalancersv2_panel.py;
\  
fi \  
&& /var/lib/kolla/venv/bin/python /var/lib/kolla/venv/bin/manage.py
collectstatic \--noinput \--clear \  
&& (cd /var/lib/kolla/venv/lib/python2.7/site-packages/horizon &&
/var/lib/kolla/venv/bin/python /var/lib/kolla/venv/bin/manage.py
compilemessages) \  
&& (cd /var/lib/kolla/venv/lib/python2.7/site-packages/openstack_dashboard &&
/var/lib/kolla/venv/bin/python /var/lib/kolla/venv/bin/manage.py
compilemessages) \  
&& chown -R horizon: /etc/openstack-dashboard /home/horizon
/var/lib/kolla/venv/lib/python2.7/site-packages/static  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start  
  
  

