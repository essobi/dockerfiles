FROM ubuntu:16.04  
MAINTAINER chris@olstrom.com  
  
# Interactive prompts don't play nice with automated build systems. Better to  
# fail and log the required configuration, so it can be added to the
Dockerfile.  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY vendor/github.com/colstrom/package.sh/bin/* /usr/local/bin/  

