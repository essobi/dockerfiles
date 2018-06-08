FROM ubuntu:trusty  
  
# Prevent dpkg errors  
ENV TERM=xterm-256color  
  
# Install Ansible  
RUN apt-get update -qy && \  
apt-get install -qy software-properties-common && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get update -qy && \  
apt-get install -qy ansible  
  
COPY ./probe.yml /ansible/  
  
WORKDIR /ansible  
  
ENTRYPOINT ["ansible-playbook"]  
  
CMD ["probe.yml"]  

