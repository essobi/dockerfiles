FROM debian:jessie  
  
MAINTAINER Cargonauts cargonauts@xebia.com  
  
ENV ANSIBLE_VERSION 1.9.0.1  
ENV ANSIBLE_CONFIG /ansible.cfg  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends python python-pip python-crypto
openssh-client sshpass && \  
pip install ansible==${ANSIBLE_VERSION}  
  
ADD ansible.cfg /ansible.cfg  
  
ADD run.sh /run.sh  
  
RUN chmod 755 /run.sh  
  
ENTRYPOINT ["/run.sh"]  

