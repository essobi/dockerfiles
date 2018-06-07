FROM ubuntu:xenial  
MAINTAINER make.io <info@make.io>  
  
ENV HADOLINT_VERSION=1.2.1  
RUN apt-get update -qq -y \  
&& apt-get install -y --no-install-recommends \  
lsb-release \  
ca-certificates \  
apt-transport-https \  
curl \  
git \  
bash \  
libgmp-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -L -o /usr/local/bin/hadolint
https://github.com/lukasmartinelli/hadolint/releases/download/v"${HADOLINT_VERSION}"/hadolint_linux_amd64  
  
RUN chmod +x /usr/local/bin/hadolint  

