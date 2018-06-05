FROM debian:jessie  
  
# Installing the 'apt-utils' package gets rid of the 'debconf: delaying
package configuration, since apt-utils is not installed'  
# error message when installing any other package with the apt-get package
manager.  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
apt-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get -y update && apt-get -y install apt-utils \  
wget \  
curl \  
ntp \  
tcpdump \  
tcptraceroute \  
traceroute \  
mtr \  
ethtool \  
uptimed \  
python-dev \  
python-pip  

