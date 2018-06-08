FROM obitech/salt:ubuntu-base  
  
LABEL maintainer="obitech@f0rkd.net"  
# Update system & install dependencies  
RUN apt-get update && \  
apt-get upgrade -y \  
-o DPkg::options::="--force-confdef" \  
-o DPkg::Options::="--force-confold" && \  
apt-get install -y \  
-o DPkg::options::="--force-confdef" \  
-o DPkg::Options::="--force-confold" \  
curl  
  
# Install via bootstrap script  
# RUN curl -L https://bootstrap.saltstack.com -o bootstrap.sh && \  
# sh bootstrap.sh -X -M stable  
# Install via apt-get  
RUN apt-get install -y \  
salt-ssh \  
salt-master

