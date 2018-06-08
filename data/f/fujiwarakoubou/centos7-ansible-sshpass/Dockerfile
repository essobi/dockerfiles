FROM ansible/centos7-ansible  
  
# bug fix of centos7-ansible  
RUN echo -e '[local]\nlocalhost\n' > /etc/ansible/hosts  
  
# for ansible-playbook  
RUN yum -y install sshpass  
  
ENV ANSIBLE_HOST_KEY_CHECKING false  
  
WORKDIR /root

