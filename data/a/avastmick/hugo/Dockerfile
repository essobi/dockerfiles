FROM debian:latest  
  
MAINTAINER avastmick@outlook.com  
  
# Install pygments (for syntax highlighting)  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-
recommends python-pygments git ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download and install hugo  
ENV HUGO_VERSION 0.20  
ENV HUGO_BINARY hugo_${HUGO_VERSION}-64bit.deb  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
/tmp/hugo.deb  
  
RUN dpkg -i /tmp/hugo.deb \  
&& rm /tmp/hugo.deb  

