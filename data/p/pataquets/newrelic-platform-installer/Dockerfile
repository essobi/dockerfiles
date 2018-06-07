FROM pataquets/ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
curl \  
default-jre-headless \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
&& \  
curl -o /tmp/install-npi.sh https://download.newrelic.com/npi/release/install-
npi-linux-debian-x64.sh \  
&& \  
chmod a+x /tmp/install-npi.sh && \  
/tmp/install-npi.sh -u && \  
rm -v /tmp/install-npi.sh  
  
WORKDIR /root/newrelic-npi  

