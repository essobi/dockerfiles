FROM ubuntu:trusty  
MAINTAINER Lamberto Diwa <lambertodiwajr@gmail.com>  
  
# Prevent dpkg errors  
ENV TERM=xterm-256-color  
  
# Set mirrors to US  
RUN sed -i "s/http:\/\/archive./http:\/\/us.archive./g" /etc/apt/sources.list  
  
# Install Ansible  
RUN apt-get update -qy && \  
apt-get install -qy software-properties-common && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get update -qy && \  
apt-get install -qy ansible  
  
# Copy baked in playbooks  
COPY ansible /ansible  
  
# Add volume for Ansible playbooks  
VOLUME /ansible  
WORKDIR /ansible  
  
ENTRYPOINT ["ansible-playbook"]  
CMD ["site.yml"]  

