FROM centos:7  
ENV container docker  
LABEL maintainer="Stephen Dunne"  
  
RUN yum makecache fast \  
&& yum -y install deltarpm epel-release initscripts \  
&& yum -y install \  
ansible sudo which git \  
python-pip \  
&& yum clean all  
  
RUN pip install ansible-lint  
  
# Disable requiretty.  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
# Install Ansible inventory file.  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
  
STOPSIGNAL SIGRTMIN+3  
CMD ["/usr/sbin/init"]  

