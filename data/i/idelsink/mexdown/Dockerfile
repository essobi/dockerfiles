FROM fedora:25  
MAINTAINER Ingmar Delsink https://github.com/idelsink  
LABEL version="1.0" \  
description="mexdown docker image"  
  
RUN dnf -y install \  
curl \  
findutils \  
git \  
sudo \  
which && \  
curl -s
https://raw.githubusercontent.com/idelsink/mexdown/master/install_latex.sh | \  
bash /dev/stdin YES && \  
dnf clean all  
  
WORKDIR /workspace  

