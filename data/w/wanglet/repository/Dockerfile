FROM ubuntu:16.04  
RUN apt-get update  
  
RUN apt-get -y install rng-tools reprepro createrepo python-pip python-dev
libffi-dev libssl-dev  
  
RUN pip install pip2pi  
RUN pip install --upgrade setuptools  
  
COPY keys /keys/  
  
RUN gpg --allow-secret-key-import --import /keys/private.key  

