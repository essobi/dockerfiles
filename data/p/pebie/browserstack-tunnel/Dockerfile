FROM ekino/docker-buildbox:latest-node5.7  
MAINTAINER Mikaël Bouchez <bouchez@ekino.com>  
  
# Install tools  
RUN echo "Install Tools" \  
&& apt-get update && apt-get upgrade -y \  
&& apt-get install -y wget unzip vim  
  
# Install BrowserStackLocal  
RUN cd /usr/local/bin \  
&& wget https://www.browserstack.com/browserstack-local/BrowserStackLocal-
linux-x64.zip \  
&& unzip BrowserStackLocal-linux-x64.zip \  
&& chmod +x BrowserStackLocal && rm BrowserStackLocal-linux-x64.zip  

