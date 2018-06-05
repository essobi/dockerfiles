FROM ubuntu:14.04  
RUN apt-get -y update \  
&& apt-get install -y \  
python-yaml \  
python-jinja2 \  
python-httplib2 \  
python-keyczar \  
python-paramiko \  
python-setuptools \  
python-pkg-resources \  
git \  
curl \  
python-pip \  
sshpass \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
####  
# Get master branch from the GutHub or download specific release as .tar.gz  
####  
ARG VERSION=master  
RUN if [ ${VERSION} = "master" ]; then \  
mkdir /opt/ansible/ && cd /opt/ansible/ \  
&& git clone https://github.com/ansible/ansible.git \  
&& cd /opt/ansible/ansible \  
&& git submodule update --init \  
&& rm -rf .git/ \  
; else \  
mkdir /opt/ansible/ && cd /opt/ansible/ \  
&& curl -o ansible.tar.gz -L
https://github.com/ansible/ansible/archive/$VERSION.tar.gz \  
&& mkdir ansible \  
&& tar -xf ansible.tar.gz --strip-components=1 -C ./ansible \  
;fi  
  
RUN mkdir /etc/ansible/ && echo '[local]\nlocalhost\n' > /etc/ansible/hosts  
  
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin  
ENV PYTHONPATH /opt/ansible/ansible/lib  
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library  
  
RUN mkdir /ansible  
WORKDIR /ansible  

