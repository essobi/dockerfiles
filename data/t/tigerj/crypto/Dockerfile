# fixed base image  
FROM ubuntu:16.04  
# apt-get installs for ubuntu  
RUN apt-get update && apt-get -y install \  
openssl='1.0.2g-1ubuntu4' \  
gnupg2='2.1.11-6ubuntu2' \  
git \  
curl \  
wget \  
pv \  
ascii \  
nano \  
vim \  
python python-dev python-pip python-stepic python-virtualenv  
  
# install python crypto tools  
COPY requirements.txt /usr/src  
RUN pip install -r /usr/src/requirements.txt  
  
# upload crypto source and link  
COPY crypto.sh /usr/src  
RUN ln /usr/src/crypto.sh /usr/bin/encrypt  
RUN ln /usr/src/crypto.sh /usr/bin/decrypt  
  
# make working dir  
RUN mkdir -p /home/crypto  
WORKDIR /home/crypto  

