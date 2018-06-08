FROM php:5.4.45  
MAINTAINER Jean-Marc Lagace <jmlagace@maysys.com>  
  
ENV DEV_TOOLS_VERSION=1.0.3  
  
RUN apt-get update && apt-get install -y git-core \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -L https://github.com/jmlagace/dev-
tools/archive/v$DEV_TOOLS_VERSION.tar.gz | tar -xz -C /tmp \  
&& mv /tmp/dev-tools-$DEV_TOOLS_VERSION/* /usr/local/bin/ \  
&& rm -rf mv /tmp/dev-tools-$DEV_TOOLS_VERSION \  
&& chmod +x /usr/local/bin/*  

