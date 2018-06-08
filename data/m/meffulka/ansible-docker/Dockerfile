FROM ubuntu:16.04  
  
MAINTAINER Alekseii Erokhin <zmeffulka@gmail.com>  
  
  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -y -q \  
build-essential \  
python python-dev \  
libffi-dev libssl-dev \  
libxml2-dev libxslt1-dev zlib1g-dev \  
git wget && \  
wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate && \  
python get-pip.py && \  
rm get-pip.py && \  
pip install --upgrade setuptools pip wheel && \  
pip install --upgrade pyyaml jinja2 pycrypto && \  
pip install --upgrade pywinrm && \  
git clone git://github.com/ansible/ansible.git --recursive && \  
cd ansible && \  
bash -c 'source ./hacking/env-setup' && \  
mkdir -p /opt/ansible && \  
mv /ansible/bin /opt/ansible/bin && \  
mv /ansible/lib /opt/ansible/lib && \  
mv /ansible/docs /opt/ansible/docs && \  
rm -rf /ansible && \  
apt-get install -y sshpass openssh-client && \  
apt-get remove -y --auto-remove \  
build-essential python-pip python-dev libffi-dev libssl-dev wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ANSIBLE_HOST_KEY_CHECKING false  
ENV PATH /opt/ansible/bin:$PATH  
ENV PYTHONPATH /opt/ansible/lib:$PYTHONPATH  
ENV MANPATH /opt/ansible/docs/man:$MANPATH  
  
# default command: display Ansible version  
CMD [ "ansible-playbook", "--version" ]  

