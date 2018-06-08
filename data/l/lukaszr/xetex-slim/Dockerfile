#  
# XeTeX on Debian 7 (Wheezy)  
# slim container  
#  
# URL: https://github.com/lukaszroz/docker-xetex-slim  
# Version: 1  
#  
# Pull base image  
FROM debian:wheezy  
  
MAINTAINER Lukasz Rozycki <docker AT lukaszr DOT com>  
  
# Install XeTeX  
RUN \  
echo "===> Update repositories" && \  
apt-get update && \  
\  
\  
echo "===> Install XeTeX" && \  
DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends install -y
--force-yes \  
texlive-xetex \  
texlive-latex-recommended \  
latex-xcolor \  
texlive-latex-extra \  
lmodern && \  
\  
\  
echo "===> Clean up" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Default command  
CMD ["xetex"]  

