FROM ubuntu:16.04  
  
RUN apt-get update && apt-get install -y \  
openssh-client \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p ~/.ssh \  
&& touch ~/.ssh/known_hosts \  
&& chmod 700 ~/.ssh \  
&& chmod 644 ~/.ssh/known_hosts

