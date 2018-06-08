FROM ruby:latest  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY bundle_config /usr/local/bundle/config  
  
RUN mkdir -p /workdir  
  
WORKDIR /workdir  

