# Pull base image.  
FROM alpine:latest  
  
MAINTAINER Dominik Hahn <dominik@monostream.com>  
  
# Install dependencies  
RUN apk add --quiet --no-cache sudo python py-pip openssl bash ca-certificates
sshpass openssh-client rsync && \  
apk add --quiet --no-cache --virtual build-dependencies python-dev libffi-dev
openssl-dev build-base && \  
pip install --upgrade pip cffi && \  
pip install ansible && \  
pip install --upgrade pywinrm netaddr && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/* /tmp/* && \  
mkdir -p /etc/ansible && \  
echo 'localhost' > /etc/ansible/hosts  
  
# Define working directory.  
WORKDIR /workspace  
  
# Executing defaults  
CMD [ "ansible-playbook", "--version" ]

