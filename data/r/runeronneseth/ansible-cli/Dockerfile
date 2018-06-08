FROM alpine:latest  
  
MAINTAINER Rune Rønneseth <rune.ronneseth@kred.no>  
  
WORKDIR /srv/ansible  
  
RUN apk --no-cache add \  
python3 \  
py3-yaml \  
py3-pip \  
openssl-dev \  
&& \  
apk --no-cache add --virtual .build-deps \  
make \  
g++ \  
python3-dev \  
libffi-dev \  
&& \  
pip3 install --no-cache-dir --upgrade pip && \  
pip3 install --no-cache-dir --upgrade setuptools && \  
pip3 install --no-cache-dir --upgrade ansible \  
&& \  
apk del .build-deps  
  
RUN mkdir -p playbooks inventory roles \  
&& \  
cp /usr/lib/python3.6/site-
packages/ansible/galaxy/data/container_enabled/tests/ansible.cfg ./ansible.cfg
\  
&& \  
printf '%s\n' \  
'all:' \  
' hosts:' \  
' master:' \  
' ansible_connection: local' \  
' ansible_python_interpreter: /usr/bin/python3' >> ./inventory/hosts  

