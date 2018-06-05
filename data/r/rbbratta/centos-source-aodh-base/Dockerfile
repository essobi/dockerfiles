FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
  
RUN yum -y install httpd mod_wsgi python-ldappool && yum clean all  
RUN mkdir -p /var/www/cgi-bin/aodh \  
&& sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
RUN mkdir -p /aodh-base-source && git clone
git://git.openstack.org/openstack/aodh /aodh-base-source/aodh-base && pushd
/aodh-base-source/aodh-base && git checkout
caf9f2e1c252835bda8d2b17b7d1239fcaa9a9ba && popd  
  
RUN ln -s aodh-base-source/* aodh \  
&& useradd --user-group aodh \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt pymongo /aodh \  
&& mkdir -p /etc/aodh /var/log/kolla/aodh /var/www/cgi-bin/aodh /home/aodh \  
&& cp -r /aodh/etc/aodh/* /etc/aodh/ \  
&& cp /aodh/aodh/api/app.wsgi /var/www/cgi-bin/aodh \  
&& chown -R aodh: /etc/aodh /var/log/kolla/aodh /var/www/cgi-bin/aodh
/home/aodh  
  
RUN usermod -a -G kolla aodh  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
COPY aodh_sudoers /etc/sudoers.d/kolla_aodh_sudoers  
  
RUN usermod -a -G kolla aodh \  
&& chmod 750 /etc/sudoers.d \  
&& chmod 640 /etc/sudoers.d/kolla_aodh_sudoers \  
&& chmod 755 /var/www/cgi-bin/aodh \  
&& touch /usr/local/bin/kolla_aodh_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_aodh_extend_start  

