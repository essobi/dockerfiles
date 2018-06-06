FROM centos:7  
MAINTAINER lyon "ll_nwpu@163.com"  
  
RUN set -x \  
&& yum install -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm \  
&& yum install -y http://rdo.fedorapeople.org/openstack-kilo/rdo-release-
kilo.rpm \  
&& yum install -y openstack-selinux \  
&& yum install -y mariadb MySQL-python hostname puppet facter \  
&& puppet module install puppetlabs-inifile  

