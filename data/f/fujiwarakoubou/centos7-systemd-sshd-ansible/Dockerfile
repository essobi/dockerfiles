FROM fujiwarakoubou/centos7-systemd-sshd  
  
# official ansible dockerfile  
RUN yum clean all && \  
yum -y install epel-release && \  
yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-
paramiko python-setuptools git python-pip  
RUN mkdir /etc/ansible/  
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts  
RUN mkdir /opt/ansible/  
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible  
WORKDIR /opt/ansible/ansible  
RUN git submodule update --init  
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin  
ENV PYTHONPATH /opt/ansible/ansible/lib  
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library  
  
# bug fix of official ansible  
RUN echo -e '[local]\nlocalhost\n' > /etc/ansible/hosts  
  
# for ansible-playbook  
RUN yum -y install sshpass python-passlib  
  
# known_hosts problem  
ENV ANSIBLE_HOST_KEY_CHECKING false  
  
WORKDIR /root  
  
CMD ["/usr/sbin/init"]

