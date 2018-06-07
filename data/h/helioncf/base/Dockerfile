# Base image for other Stackato images.  
#  
# The base image serves two purposes:  
# * Install common packages to minimize size of other images  
# * Potentially add configuration as environment variables  
  
FROM helioncf/ubuntu-core  
  
# For future use.  
ENV STACKATO_DOCKER True  
  
RUN add-apt-repository \--yes ppa:git-core/ppa \  
&& add-apt-repository \--yes ppa:evarlast/golang1.4 \  
&& apt-get update \  
&& apt-get install --assume-yes bzr git golang mercurial wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD stackon.json /  

