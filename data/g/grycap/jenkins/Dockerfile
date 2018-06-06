FROM grycap/jenkins:ubuntu16.04-base  
LABEL description="Container with the latest version of Git"  
MAINTAINER Alfonso Pérez (alpegon3@upv.es)  
  
# Add the Ansible PPA  
RUN sudo apt-add-repository -y ppa:ansible/ansible  
  
# Update and install all the necessary packages  
RUN apt-get update && apt-get install -y \  
ansible \  
vim \  
nano \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

