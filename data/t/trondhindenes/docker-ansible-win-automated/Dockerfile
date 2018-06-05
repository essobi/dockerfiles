# Latest Ubuntu LTS  
FROM ubuntu:14.04  
MAINTAINER Trond Hindenes <trond@hindenes.com>  
#Setup things  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
ENV DEBIAN_FRONTEND noninteractive  
  
#Packages  
RUN apt-get -y update && \  
apt-get install -y python-yaml python-jinja2 python-httplib2 python-keyczar
python-paramiko python-setuptools python-pkg-resources git python-pip nano
sshpass  
  
#Packages for windows  
#RUN sudo apt-get install krb5-user -y  
#RUN sudo apt-get install libkrb5-dev -y  
#Python Packages  
RUN pip install http://github.com/diyan/pywinrm/archive/master.zip#egg=pywinrm  
#RUN sudo pip install kerberos  
#Set the root pass  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
RUN mkdir /etc/ansible/  
RUN mkdir /etc/ansible/inventory  
RUN mkdir /etc/ansible/modules  
RUN touch /etc/ansible/inventory/hosts  
RUN mkdir /opt/ansible/  
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible  
  
WORKDIR /opt/ansible/ansible  
RUN git submodule update --init  
  
WORKDIR /opt/ansible/modules  
RUN git clone https://github.com/trondhindenes/ansible-arm-deployment.git
ansible_arm  
RUN git clone https://github.com/trondhindenes/Ansible-Auto-Generated-
Modules.git dsc_modules  
  
WORKDIR /tmp  
RUN wget https://raw.githubusercontent.com/trondhindenes/docker-
ansible_win/master/ansible.cfg  
#RUN wget http://hindenes.com/files/krb5.conf  
#RUN wget http://hindenes.com/files/hosts  
RUN wget
https://raw.githubusercontent.com/trondhindenes/armrest/master/AnsibleInventory/arminventory.py  
  
#RUN cp krb5.conf /etc  
RUN cp ansible.cfg /etc/ansible  
#RUN cp hosts /etc/ansible/inventory  
RUN cp arminventory.py /etc/ansible/inventory  
RUN chmod +x /etc/ansible/inventory/arminventory.py  
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin  
ENV PYTHONPATH /opt/ansible/ansible/lib  
  
WORKDIR /opt/ansible/  

