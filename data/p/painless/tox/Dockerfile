FROM themattrix/tox-base  
  
LABEL maintainer "Peter Bittner <peter@painless.software>"  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
git \  
ca-certificates \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

