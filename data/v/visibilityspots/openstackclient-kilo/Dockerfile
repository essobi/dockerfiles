FROM centos:7  
LABEL author="Jan Collijs"  
  
COPY CentOS-OpenStack-Kilo.repo /etc/yum.repos.d/CentOS-OpenStack-Kilo.repo  
  
RUN set -x \  
&& yum install -y bash-completion \  
&& yum install -y
http://vault.centos.org/centos/7.3.1611/cloud/x86_64/openstack-kilo/centos-
release-openstack-kilo-1-2.el7.noarch.rpm \  
&& yum install -y python-novaclient \  
&& yum install -y python-ceilometerclient \  
&& yum install -y python-cinderclient \  
&& yum install -y python-glanceclient \  
&& yum install -y python-heatclient \  
&& yum install -y python-ironicclient \  
&& yum install -y python-keystoneclient \  
&& yum install -y python-manilaclient \  
&& yum install -y python-novaclient \  
&& yum install -y python-openstackclient \  
&& yum install -y python-saharaclient \  
&& yum install -y python-troveclient \  
&& yum install -y python-zaqarclient \  
&& yum clean all \  
&& useradd client  
  
USER client  
  
ENTRYPOINT ["bash", "--rcfile", "/home/client/.keystonerc"]  

