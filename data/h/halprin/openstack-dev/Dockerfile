FROM ubuntu  
MAINTAINER halprin  
  
#update the repositories and install...  
RUN apt-get update && apt-get install -y \  
  
#install python  
python3.5 \  
python3.4 \  
python3-pip \  
python \  
python-pip \  
  
#install git  
git \  
git-review \  
  
#install OpenStack required libraries  
libpq-dev \  
gettext \  
libffi6 \  
libffi-dev \  
  
#install nice-to-have stuff since this is an interactive container  
vim \  
man  
  
#update pip3 and install...  
RUN pip3 install --upgrade pip && pip3 install \  
tox \  
bindep  
  
#update pip2 and install...  
RUN pip2 install --upgrade pip && pip2 install \  
tox \  
bindep  
  
RUN mkdir /usr/local/src/openstack/  
  
VOLUME /usr/local/src/openstack/  
WORKDIR /usr/local/src/openstack/  
ENTRYPOINT ["/bin/bash"]  

