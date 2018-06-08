FROM debian:stretch-slim  
  
RUN sed -i -e 's/^deb \\(.*\\)/deb \1\ndeb-src \1/' /etc/apt/sources.list && \  
apt-get update && apt-get -y dist-upgrade && \  
apt-get --no-install-recommends -y install devscripts && \  
apt-get --no-install-recommends -y build-dep linux && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  

