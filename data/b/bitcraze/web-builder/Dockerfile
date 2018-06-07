FROM ruby:2.4.3  
MAINTAINER Kristoffer Richardsson <kristoffer@bitcraze.io>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
php5 \  
zip unzip \  
locales \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install docker (see https://github.com/docker-library/docker)  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.10.3  
ENV DOCKER_SHA256
d0df512afa109006a450f41873634951e19ddabf8c7bd419caeb5a526032d86d  
RUN curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION" -o
/usr/local/bin/docker \  
&& echo "${DOCKER_SHA256} /usr/local/bin/docker" | sha256sum -c - \  
&& chmod +x /usr/local/bin/docker  
  
# Set the locale to make ruby open text files as UTF-8 default  
# (Encoding.default_external). Required to make html-proofer handle UTF-8.  
ENV LANG C.UTF-8  
RUN gem install jekyll jekyll-feed html-proofer  
  
WORKDIR /module  

