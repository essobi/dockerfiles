FROM ubuntu:xenial  
MAINTAINER Rene Meza <rene.meza125@gmail.com>  
  
# Prevent dpkg errors  
ENV TERM=xterm-256color  
  
# Set mirrors to NZ  
RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list  
  
# Install dependencies  
RUN apt-get update -qy && \  
apt-get install -qy software-properties-common && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get update -qy && \  
apt-get install -qy ansible  
  
# Copy playbooks  
COPY playbooks /playbooks  
  
# Add volume for Ansible playbooks  
VOLUME /playbooks  
WORKDIR /playbooks  
  
# Entrypoint  
ENTRYPOINT ["ansible-playbook"]  
CMD ["site.yml"]  
  

