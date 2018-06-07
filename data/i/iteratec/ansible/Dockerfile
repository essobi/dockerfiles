FROM ubuntu:16.04  
MAINTAINER Thomas Steinbach (@aikq.de)  
  
# install requirements from repos  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
git \  
ssh-client \  
vim \  
python-pip \  
python-docker \  
apt-transport-https && \  
apt-key adv \  
\--keyserver hkp://p80.pool.sks-keyservers.net:80 \  
\--recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \  
echo 'deb https://apt.dockerproject.org/repo debian-jessie main' >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y docker-engine && \  
apt-get clean && \  
apt-get autoremove  
  
# install requirements from pip  
RUN pip install paramiko PyYAML Jinja2 httplib2 six  
RUN pip install paramiko==2.0.0 \  
PyYAML==3.11 \  
Jinja2==2.8 \  
httplib2==0.9.2 \  
six==1.10.0 \  
markupsafe==0.23 \  
pycrypto==2.6.1  
  
RUN adduser --disabled-password --gecos '' uid1000  
  
# create ansibles default inventory dummy  
RUN mkdir -p /etc/ansible && \  
touch /etc/ansible/hosts && \  
chown uid1000:uid1000 /etc/ansible/hosts  
  
# add start script  
ADD start.sh /usr/local/bin/start.sh  
RUN chmod 0655 /usr/local/bin/start.sh  
  
# create directories for Ansible repositories  
RUN mkdir /ansible && \  
mkdir /ansible-artifacts && \  
chown uid1000:uid1000 /ansible && \  
chown uid1000:uid1000 /ansible-artifacts  
  
USER uid1000  
  
# clone official repository  
RUN git clone \--recursive git://github.com/ansible/ansible.git /ansible && \  
cd /ansible && \  
git reset --hard v2.3.1.0-1  
  
WORKDIR /  
ENTRYPOINT ["start.sh"]  

