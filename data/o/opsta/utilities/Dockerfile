# Ubuntu with various of client application  
#  
# Ansible  
# Docker client  
# Docker machine  
# Docker compose  
# Shade (Client for OpenStack)  
  
FROM ubuntu:xenial-20160923.1  
MAINTAINER Jirayut Nimsaeng <jirayut [at] opsta.io>  
  
# 1) Install utility commands and necessary packages  
# 2) Download Docker client, machine and compose  
# 3) Install Ansible and necessary python libraries  
# 4) Clean to reduce size of Docker Image  
# 5) Work around Ansible doesn't play very well with overlayfs  
# https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1214500  
ARG APT_CACHER_NG  
ARG DEVPI_SERVER  
ENV ANSIBLE_HOST_KEY_CHECKING=False \  
DOCKER_ENGINE_VERSION=1.12.1 \  
DOCKER_COMPOSE_VERSION=1.8.1 \  
DOCKER_MACHINE_VERSION=0.8.2 \  
OPSTA_PLAYBOOK_ANSIBLE_COMMIT_ID=ddec77f8ba22c65f65537a2574b609c4a840e398 \  
OPSTA_PLAYBOOK_PYTHON_COMMIT_ID=1042d06f8803ae49ba152c0f7cb8c7d623d5ff21  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
[ -n "$DEVPI_SERVER" ] && \  
mkdir -p ~/.pip && \  
echo "[global]\n\  
index-url = $DEVPI_SERVER\n\  
trusted-host = \  
$(echo $DEVPI_SERVER | awk -F/ '{print $3}' | awk -F: '{print $1}')\n\  
" >> ~/.pip/pip.conf || true; \  
apt-get update && \  
apt-get install -y vim socat python python-dev curl wget git sshpass \  
libssl-dev libffi-dev build-essential && \  
wget -O /usr/local/bin/docker.tgz \  
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_ENGINE_VERSION.tgz
&& \  
wget -O /usr/local/bin/docker-compose \  
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-`uname -s`-`uname -m` && \  
wget -O /usr/local/bin/docker-machine \  
https://github.com/docker/machine/releases/download/v$DOCKER_MACHINE_VERSION/docker-
machine-`uname -s`-`uname -m` && \  
tar xvfz /usr/local/bin/docker.tgz -C /usr/local/bin/ --strip=1 && \  
chmod +x /usr/local/bin/docker-compose /usr/local/bin/docker-machine && \  
mkdir -p /etc/ansible/requirements /etc/ansible/scripts && \  
wget -O /etc/ansible/requirements/python-requirements.txt \  
https://raw.githubusercontent.com/opsta/opsta-
playbook/$OPSTA_PLAYBOOK_PYTHON_COMMIT_ID/requirements/python-requirements.txt
&& \  
cd /etc/ansible/scripts && \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
curl https://raw.githubusercontent.com/opsta/opsta-
playbook/$OPSTA_PLAYBOOK_ANSIBLE_COMMIT_ID/scripts/install-ansible.sh | bash
&& \  
apt-get remove --purge --auto-remove -y \  
build-essential ifupdown iproute2 isc-dhcp-client isc-dhcp-common \  
libatm1 libisc-export160 libmnl0 libxtables11 manpages netbase \  
python-dev libssl-dev libffi-dev && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /usr/lib/x86_64-linux-gnu/libfakeroot /var/lib/apt/lists/* \  
/etc/apt/apt.conf.d/11proxy /root/.cache /root/.pip \  
/etc/ansible/requirements /etc/ansible/scripts  
COPY files/ansible.cfg /etc/ansible/ansible.cfg  

