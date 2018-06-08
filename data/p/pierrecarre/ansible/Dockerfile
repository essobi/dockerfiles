FROM centos:centos7  
MAINTAINER Pierre CARRE <pierre.carre78@gmail.com>  
  
RUN echo "===> Installing EPEL..." && \  
yum -y install epel-release && \  
\  
\  
echo "===> Installing Ansible dependencies..." && \  
yum -y install sudo make python-devel python-httplib2 python-paramiko python-
jinja2 python-crypto2.6 PyYAML python-setuptools python-keyczar && \  
\  
\  
echo "===> Installing Ansible..." && \  
curl -o /tmp/ansible.tar.gz
http://releases.ansible.com/ansible/ansible-1.8.4.tar.gz && \  
\  
\  
echo "===> Untar Ansible archive..." && \  
cd /tmp && \  
tar xzvf ansible.tar.gz && \  
\  
\  
echo "===> Install Ansible..." && \  
cd ansible-*/ && \  
make install && \  
\  
\  
echo "===> Disabling sudo 'requiretty' setting..." && \  
sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers && \  
\  
\  
echo "===> Removing archive..." && \  
rm -rf /tmp/ansible-* && \  
\  
\  
echo "===> Removing unused YUM resources..." && \  
yum -y remove epel-release && \  
yum clean all && \  
\  
\  
echo "===> Adding hosts for convenience..." && \  
mkdir -p /etc/ansible && \  
echo '[local]\nlocalhost\n' > /etc/ansible/hosts  
  
  
# default command: display Ansible version  
CMD [ "ansible-playbook", "--version" ]  

