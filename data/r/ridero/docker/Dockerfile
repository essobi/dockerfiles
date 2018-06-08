FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN \  
locale-gen en_US.UTF-8  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
curl \  
wget \  
dnsutils \  
vim-tiny \  
apt-transport-https \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN set -x \  
&& cd /tmp \  
&& wget https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-
init_1.0.0_amd64.deb \  
&& dpkg -i dumb-init_*.deb \  
&& rm -Rf dumb-init_*.deb  
  
CMD [ "/bin/bash" ]  

