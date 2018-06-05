FROM alpine:3.5  
  
MAINTAINER Ryan Boyle <ryan@boyle.io>  
  
# add dependencies to be removed by packer  
RUN apk --update add \--virtual ansible-dependencies\  
python \  
py-pip \  
openssl \  
bash \  
ca-certificates && \  
# add dependencies to be removed  
apk --update add \--virtual build-dependencies \  
python-dev \  
libffi-dev \  
openssl-dev \  
git \  
build-base && \  
  
pip install --upgrade pip cffi && \  
  
# create dir for ansible. Will be removed by packer.  
mkdir -p /opt && \  
  
cd /opt && \  
  
git clone https://github.com/ansible/ansible.git --recursive && \  
  
cd /opt/ansible && \  
  
pip install -r ./requirements.txt && \  
  
# source ansible  
echo "cd /opt/ansible/ && source hacking/env-setup" >> /etc/profile.d/nve.sh
&& \  
chmod +x /etc/profile.d/nve.sh && \  
  
  
#cleanup  
apk del build-dependencies && \  
rm -rf /var/cache/apk/*  

