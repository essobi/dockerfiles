# Dockerizing a base images with:  
#  
# - Debian Stretch  
# - bzr, git, mercurial, openssh-client, subversion  
#  
# Build: docker build -t ermac/debian:stretch-scm .  
#  
# https://github.com/docker-library/buildpack-deps  
#  
  
FROM ermac/debian:stretch-curl  
  
MAINTAINER Fabio Martino <fabiomartino@libero.it>  
  
# procps is very common in build systems, and is a reasonably small package  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
bzr \  
git \  
mercurial \  
openssh-client \  
subversion \  
procps \  
&& rm -rf /var/lib/apt/lists/*

