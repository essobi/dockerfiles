FROM ubuntu:16.04  
ENV TERM linux  
ENV ENV DEBIAN_FRONTEND noninteractive  
  
  
COPY install_debian_script.sh /usr/local/bin/  
  
# Install Server Dependencies for Onyx  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -yq --no-install-recommends \  
supervisor \  
dnsmasq \  
avrdude \  
jq \  
pulseaudio \  
alsa-utils && \  
cd /usr/local/bin && \  
/bin/bash install_debian_script.sh && \  
  
mkdir /onyx && \  
TOP=/onyx && \  
cd /onyx && \  
  
# Checkout Onyx  
git clone https://github.com/OnyxProject/Onyx.git /onyx/ai && \  
cd /onyx/ai && \  
easy_install pip==7.1.2  
COPY setup.sh /onyx/ai/  
RUN \  
cd /onyx/ai && \  
/bin/bash setup.sh  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
WORKDIR /onyx/ai  
ENV PYTHONPATH $PYTHONPATH:/onyx/ai  
EXPOSE 8080  
CMD ["/usr/bin/supervisord"]  

