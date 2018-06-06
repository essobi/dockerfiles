FROM bitriseio/docker-bitrise-base:latest  
  
LABEL \  
maintainer="mickare"  
  
RUN apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
build-essential \  
clang \  
cmake  
  
CMD bitrise --version

