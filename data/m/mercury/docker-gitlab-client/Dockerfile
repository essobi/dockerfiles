FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Ruby and Gem  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-utils \  
software-properties-common \  
&& apt-get install -y --no-install-recommends \  
ruby \  
gem \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install gitlab client  
RUN gem install gitlab  
  
# Set workdir and unset entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  

