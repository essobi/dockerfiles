FROM finmason/alpine_jenkins_swarm_agent  
  
ENV TERRAFORM_VERSION=0.9.2  
USER root  
  
RUN apk --update add --no-cache \  
ca-certificates \  
git \  
openssl \  
py2-pip \  
python2 && \  
apk --update add \--virtual build-dependencies\  
build-base \  
libffi-dev \  
openssl-dev \  
python2-dev  
  
RUN pip install --upgrade pip cffi  
  
RUN pip install \  
ansible==2.2.1 \  
doit==0.29.0 && \  
apk del build-dependencies  
  
RUN cd /tmp && \  
wget
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /var/tmp/* && \  
rm -rf /home/jenkins/.cache  
  
USER jenkins  

