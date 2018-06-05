FROM ubuntu:16.04  
MAINTAINER Frankie Robertson <frankie@robertson.name>  
  
RUN apt-get update && apt-get install -y \  
wget \  
curl \  
sudo \  
&& wget http://apertium.projectjj.com/apt/install-nightly.sh -O - | sudo bash
\  
&& apt-get update \  
&& apt-get -f install -y apertium-all-dev apertium-en-es apertium-rus
apertium-ukr \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

