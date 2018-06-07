FROM ubuntu:18.04  
MAINTAINER David Esler <david.esler@starlab.io>  
  
RUN mkdir /source && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qq install -y \  
\--no-install-recommends make doxygen graphviz \  
texlive-latex-recommended texlive-latex-extra \  
texlive-fonts-recommended texlive-fonts-extra texlive-lang-all && \  
apt-get -qq autoremove -y && apt-get -qq clean && \  
rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*  
  
VOLUME ["/source"]  
WORKDIR /source  
CMD ["/bin/bash"]  

