FROM huangxiangyu/compass-tasks:v0.2  
#FROM localbuild/compass-tasks  
RUN yum install https://rdoproject.org/repos/openstack-ocata/rdo-release-
ocata.rpm -y && \  
yum install git ntp ntpdate openssh-server python-devel sudo '@Development
Tools' -y  
  
# git clone openstack-ansible  
RUN git clone https://git.openstack.org/openstack/openstack-ansible
/opt/openstack-ansible  
  
#checkout to ocaata branch  
RUN cd /opt/openstack-ansible && \  
git checkout -b ocata remotes/origin/stable/ocata  
  
RUN /bin/cp -rf /opt/openstack-ansible/etc/openstack_deploy
/etc/openstack_deploy  
  
#bootstrap to download the install module and posting openstack-ansible  
RUN cd /opt/openstack-ansible && \  
scripts/bootstrap-ansible.sh  
  
RUN rm -f /usr/local/bin/ansible-playbook  
  
RUN cd /opt/openstack-ansible/scripts/ && \  
python pw-token-gen.py --file /etc/openstack_deploy/user_secrets.yml  

