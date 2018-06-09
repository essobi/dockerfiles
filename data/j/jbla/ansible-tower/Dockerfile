FROM ubuntu:14.04  
MAINTAINER Julien Blanc <jbla@tuta.io>  
  
ENV ANSIBLE_TOWER_VER 3.1.3  
EXPOSE 80 443  
RUN yes | apt-get update \  
&& yes | apt-get install software-properties-common \  
&& yes | apt-add-repository ppa:ansible/ansible \  
&& yes | apt-get update \  
&& yes | apt-get install ansible wget libpython2.7  
  
RUN yes | apt-get install ssh \  
&& mkdir ~/.ssh \  
&& service ssh start \  
&& ssh-keyscan -H 127.0.0.1 > ~/.ssh/known_hosts \  
&& service ssh stop  
  
WORKDIR /opt  
  
RUN wget https://releases.ansible.com/awx/setup/ansible-tower-
setup-${ANSIBLE_TOWER_VER}.tar.gz  
RUN tar xvzf ansible-tower-setup-${ANSIBLE_TOWER_VER}.tar.gz \  
&& rm -rf ansible-tower-setup-${ANSIBLE_TOWER_VER}.tar.gz \  
&& mv ansible-tower-setup-${ANSIBLE_TOWER_VER} /opt/ansible-tower  
  
ADD start.sh start.sh  
ADD custom.sh /opt/ansible-tower/custom.sh  
  
RUN chmod +x start.sh  
RUN chmod +x /opt/ansible-tower/custom.sh  
RUN /opt/ansible-tower/custom.sh  
RUN /opt/ansible-tower/setup.sh \  
&& rm -rf /opt/ansible-tower  
  
RUN pip install pyvmomi pysphere  
  
ENTRYPOINT exec /opt/start.sh

