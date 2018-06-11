FROM ubuntu:latest  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y -q --no-install-recommends \  
build-essential \  
git \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  

