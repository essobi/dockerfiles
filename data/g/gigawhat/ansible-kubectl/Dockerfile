FROM python:2.7.13  
ENV SERVERLESS_VERSION 1.23.0  
ENV ANSIBLE_VERSION='2.3.2.0'  
ENV KUBECTL_VERSION='v1.6.7'  
ENV DEBIAN_FRONTEND noninteractive  
  
# install node and serverless  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs zip && \  
npm install -g serverless@${SERVERLESS_VERSION} && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /root/.npm && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# install ansible and boto for aws  
RUN pip install \  
ansible==${ANSIBLE_VERSION} \  
awscli \  
datadog \  
boto \  
boto3 && \  
rm -rf /root/.cache  
  
# install kubectl  
RUN curl -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl && chmod +x
/usr/bin/kubectl  
  
# set ssh config  
COPY ssh-config /root/.ssh/config  
  
# general cleanup  
RUN rm -rf /usr/share/doc && \  
rm -rf /usr/share/man  

