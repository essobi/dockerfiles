FROM debian:jessie  
  
COPY texlive.profile /  
  
RUN PACKAGES="wget libswitch-perl" \  
&& apt-get update \  
&& apt-get install -qq $PACKAGES \--no-install-recommends \  
&& wget -qO- http://mirror.ctan.org/systems/texlive/tlnet/install-tl-
unx.tar.gz |\  
tar xz \  
&& cd install-tl-* \  
&& ./install-tl -profile /texlive.profile \  
# Cleanup  
&& rm -rf install-tl-* \  
&& apt-get remove --purge -qq $PACKAGES \  
&& apt-get autoremove --purge -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/tex  
WORKDIR /var/tex  

