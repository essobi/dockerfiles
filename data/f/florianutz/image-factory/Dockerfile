FROM alpine:3.7  
LABEL maintainer="Florian Utz"  
  
ENV PACKER_VERSION=1.1.3  
ENV
PACKER_SHA256SUM=b7982986992190ae50ab2feb310cb003a2ec9c5dcba19aa8b1ebb0d120e8686f  
  
RUN echo "===> Adding Python runtime..." && \  
apk --no-cache --upgrade add python python3 py-pip openssl ca-certificates
sudo groff && \  
apk --no-cache --upgrade add \--virtual build-dependencies \  
python-dev libffi-dev openssl-dev build-base && \  
pip install --no-cache-dir --upgrade pip cffi && \  
\  
echo "===> Installing Ansible..." && \  
pip install --no-cache-dir --upgrade ansible && \  
\  
echo "===> Installing awscli..." && \  
pip install --no-cache-dir --upgrade awscli && \  
\  
echo "===> Adding some tools..." && \  
apk --no-cache --upgrade add git wget openssl curl jq && \  
apk --no-cache upgrade && \  
\  
echo "===> Removing package list..." && \  
apk del build-dependencies && \  
echo "===> Package installation completed!"  
  
COPY setup-packer.sh /usr/local/bin/  
RUN /usr/local/bin/setup-packer.sh  
  
# Install Ansible inventory file  
# RUN mkdir /etc/ansible && echo -e '[local]\nlocalhost
ansible_connection=local' > /etc/ansible/hosts  
RUN adduser -D imagefactory && mkdir /data && chown imagefactory:imagefactory
/data && chmod 770 /data  
USER imagefactory  
WORKDIR /data  
###  
CMD ["/bin/sh"]  

