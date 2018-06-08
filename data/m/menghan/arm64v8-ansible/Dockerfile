# ref:https://github.com/William-Yeh/docker-
ansible/blob/master/ubuntu16.04-onbuild/Dockerfile  
FROM resin/aarch64-python:2.7-slim  
  
MAINTAINER Menghan Zheng <menghan412@gmail.com>  
  
  
RUN ["cross-build-start"]  
  
RUN echo "===> Adding Ansible's PPA..." && \  
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main" | tee
/etc/apt/sources.list.d/ansible.list && \  
echo "deb-src http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/ansible.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7BB9C367 &&
\  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
\  
\  
echo "===> Installing Ansible..." && \  
apt-get install -y ansible && \  
\  
\  
echo "===> Removing Ansible PPA..." && \  
rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/ansible.list && \  
\  
\  
echo "===> Adding hosts for convenience..." && \  
echo 'localhost' > /etc/ansible/hosts  
  
RUN ["cross-build-end"]  
  
COPY ansible-playbook-wrapper /usr/local/bin/  
  
ONBUILD RUN ["cross-build-start"]  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
echo "===> Updating TLS certificates..." && \  
apt-get install -y openssl ca-certificates  
  
ONBUILD WORKDIR /tmp  
ONBUILD COPY . /tmp  
ONBUILD RUN \  
echo "===> Diagnosis: host information..." && \  
ansible -c local -m setup all  
  
# default command: display Ansible version  
CMD [ "ansible-playbook", "--version" ]  

