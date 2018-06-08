FROM ubuntu:16.04  
MAINTAINER Go About <tech@goabout.com>  
  
RUN apt-get update -q && \  
apt-get install -yq software-properties-common && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get update -q && \  
apt-get install -yq ansible && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /ansible  
  
ENV ANSIBLE_PLAYBOOK site.yml  
  
CMD ["sh", "-c", "ansible-playbook \"$ANSIBLE_PLAYBOOK\""]  

