# Ubuntu with various of client application  
#  
# Ansible  
# Docker client  
# Docker machine  
# Docker compose  
# Shade (Clients for OpenStack)  
FROM winggundamth/ubuntu-base:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
# 1) Install Ansible and necessary packages  
# 2) Download Docker client, machine and compose  
# 3) Install Shade  
# 4) Clean to reduce size of Docker Image  
# 5) Install utility commands  
ARG APT_CACHER_NG  
ARG DEVPI_SERVER  
ENV ANSIBLE_HOST_KEY_CHECKING=False  
COPY files/python-requirements.txt /root/python-requirements.txt  
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
apt-get install -y vim socat python python-dev curl wget git build-essential
sshpass && \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
apt-get install -y libssl-dev libffi-dev && \  
pip install -r /root/python-requirements.txt && \  
wget -O /usr/local/bin/docker.tgz \  
https://get.docker.com/builds/Linux/x86_64/docker-1.12.1.tgz && \  
wget -O /usr/local/bin/docker-compose \  
https://github.com/docker/compose/releases/download/1.8.0/docker-
compose-`uname -s`-`uname -m` && \  
wget -O /usr/local/bin/docker-machine \  
https://github.com/docker/machine/releases/download/v0.8.1/docker-
machine-`uname -s`-`uname -m` && \  
tar xvfz /usr/local/bin/docker.tgz -C /usr/local/bin/ --strip=1 && \  
chmod +x /usr/local/bin/docker-compose /usr/local/bin/docker-machine && \  
apt-get remove --purge --auto-remove -y \  
build-essential ifupdown iproute2 isc-dhcp-client isc-dhcp-common \  
libatm1 libisc-export160 libmnl0 libxtables11 manpages netbase \  
python-dev libssl-dev libffi-dev && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /usr/lib/x86_64-linux-gnu/libfakeroot /var/lib/apt/lists/* \  
/etc/apt/apt.conf.d/11proxy /root/.cache /root/.pip \  
/root/python-requirements.txt  
  
# 1) Work around Ansible doesn't play very well with overlayfs  
# https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1214500  
# 2) Patch latest ansible docker module  
# https://github.com/ansible/ansible/issues/16865  
RUN mkdir -p /etc/ansible && \  
echo '[ssh_connection]' >> /etc/ansible/ansible.cfg && \  
echo 'ssh_args =' >> /etc/ansible/ansible.cfg && \  
PYTHON_LIB_PATH=$(echo 'import os; from ansible.playbook import play_context;
print os.path.dirname(play_context.__file__);' | python -) && \  
rm $PYTHON_LIB_PATH/play_context.pyc && \  
sed -i '417,418 s/^/#/' \  
$PYTHON_LIB_PATH/play_context.py && \  
PYTHON_LIB_PATH=$(echo 'import os; from ansible.plugins.connection import
docker; print os.path.dirname(docker.__file__);' | python -) && \  
rm $PYTHON_LIB_PATH/docker.pyc && \  
wget -O $PYTHON_LIB_PATH/docker.py \  
https://raw.githubusercontent.com/ansible/ansible/a4785c2691290df6047da5294632a8c428e67476/lib/ansible/plugins/connection/docker.py
&& \  
PYTHON_LIB_PATH=$(echo 'import os; from ansible.module_utils import
docker_common; print os.path.dirname(docker_common.__file__);' | python -) &&
\  
rm $PYTHON_LIB_PATH/docker_common.pyc && \  
wget -O $PYTHON_LIB_PATH/docker_common.py \  
https://raw.githubusercontent.com/ansible/ansible/39aa740531f171a557e8604babd493793d63323e/lib/ansible/module_utils/docker_common.py
&& \  
PYTHON_LIB_PATH=$(echo 'import os; from ansible.modules.core.cloud.docker
import docker_container; print os.path.dirname(docker_container.__file__);' |
python -) && \  
rm $PYTHON_LIB_PATH/docker_container.pyc && \  
wget -O $PYTHON_LIB_PATH/docker_container.py \  
https://raw.githubusercontent.com/ansible/ansible-modules-
core/de0122fdaf5975cf2df87fc36b059c74032396e6/cloud/docker/docker_container.py  

