FROM google/cloud-sdk:195.0.0  
  
MAINTAINER Travix  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
gettext-base \  
jq \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

