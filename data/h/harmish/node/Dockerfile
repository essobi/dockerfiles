FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y nodejs npm && \  
#  
ln -s /usr/bin/nodejs /usr/bin/node && \  
#  
# clean-up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

