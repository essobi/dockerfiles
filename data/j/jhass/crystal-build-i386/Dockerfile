FROM ioft/i386-ubuntu:16.04  
MAINTAINER Jonne Haß <me@jhass.eu>  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https curl build-essential pkg-config libssl-
dev llvm libedit-dev libgmp-dev libxml2-dev libyaml-dev libreadline-dev git-
core gdb && \  
curl https://dist.crystal-lang.org/apt/setup.sh | bash && \  
apt-get update && \  
apt-get install -y crystal  
  
CMD ["/bin/bash"]  

