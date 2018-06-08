FROM ubuntu:trusty  
MAINTAINER Anshul Sharma <optimisticanshul@gmail.com>  
  
# Prevent dkpg errors  
ENV TERM=xterm-256color  
  
RUN apt-get update -qy && \  
apt-get install -qy software-properties-common && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get update -qy && \  
apt-get install -qy ansible  
  
# Copy baked  
COPY ansible /ansible  
  
# Add volume for ansible playbooks  
VOLUME /ansible  
WORKDIR /ansible  
  
# Entrypoint  
ENTRYPOINT ["ansible-playbook"]  
CMD ["site.yml"]  

