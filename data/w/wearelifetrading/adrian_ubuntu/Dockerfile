FROM wearelifetrading/gcc5:1.5  
MAINTAINER Adrian Swain <adrian.swain@lifetrading.com.au>  
  
USER root  
  
# Install build wireshark, need to run as root  
RUN apt-get update && \  
apt-get install -y wireshark && \  
groupadd wireshark && \  
usermod -aG wireshark developer && \  
setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap && \  
chgrp wireshark /usr/bin/dumpcap && \  
chmod 750 /usr/bin/dumpcap  
  
# Install my favourite tools  
RUN apt-get update && \  
apt-get install -y htop linux-tools-generic screen valgrind  
  
# Clean up after ourselves to make the image smaller  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER developer  
  
ARG GIT_EMAIL  
ARG GIT_USER  
  
RUN git config --global user.name "${GIT_USER}" && \  
git config --global user.email "${GIT_EMAIL}"  

