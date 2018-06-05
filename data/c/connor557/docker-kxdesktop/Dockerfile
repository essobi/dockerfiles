FROM kxes/ubuntu-xrdp-base  
  
MAINTAINER josh@kxes.net  
  
# set new password  
RUN echo "root:Docker" | chpasswd  
  
# install required tools  
RUN apt-get update && apt-get install --yes --force-yes --no-install-
recommends git wget rsync && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
# install platform-client  
RUN cd /usr/bin && wget https://github.com/kxes/platform-
client/raw/master/platform-client && chmod +x platform-client  
  
# add repo and channel  
RUN platform-client --addrepo https://github.com/kxes/platform-core-
providers.git  
RUN platform-client --addchannel https://github.com/kxes/config-kxdesktop.git  
  
# configure  
RUN platform-client --configure --debug --output  

