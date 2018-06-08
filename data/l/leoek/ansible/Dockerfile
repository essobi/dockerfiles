FROM debian:9.4-slim  
  
#install the build deps  
RUN apt-get update -y && apt-get install -y make \  
git \  
make \  
python-setuptools \  
gcc \  
python-dev \  
libffi-dev \  
libssl-dev \  
python-packaging && \  
rm -rf /var/lib/apt/lists/* && \  
#build and install ansible  
mkdir -p /ansible && \  
cd /ansible/ && \  
git clone git://github.com/ansible/ansible.git && \  
cd /ansible/ansible && \  
git checkout stable-2.4 && \  
make && \  
make install && \  
rm -rf /ansible/ansible && \  
#remove dev deps  
apt-get remove -y git \  
make \  
gcc \  
libffi-dev \  
libssl-dev \  
python-dev && \  
apt-get autoremove -y  
  
RUN mkdir -p /ansible/playbooks  
WORKDIR /ansible/playbooks  
  
ENV ANSIBLE_GATHERING smart  
ENV ANSIBLE_HOST_KEY_CHECKING false  
ENV ANSIBLE_RETRY_FILES_ENABLED false  
ENV ANSIBLE_ROLES_PATH /ansible/playbooks/roles  
ENV ANSIBLE_SSH_PIPELINING True  
  
#ENTRYPOINT [ "/bin/bash" ]  
ENTRYPOINT [ "ansible-playbook" ]  
CMD [ "playbook.yml","-i","hosts","--private-key","~/.ssh/key"]

