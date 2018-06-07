# Wildfly server with additional configurations  
FROM ubuntu:16.04  
MAINTAINER Lucas Russo  
  
# User root user to install software  
USER root  
  
# Install missing dependencies  
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \  
apt-get update && apt-get install -y \  
wget \  
git \  
sudo \  
net-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
# Setup git, only for applying patches  
RUN git config --global user.email "epics-dev-docker@epics-dev-docker.com"  
RUN git config --global user.name "EPICS_DEV Docker"  
  
# Create build directory  
RUN mkdir -p /build  
  
# Copy compilation scripts to build directory  
COPY setup.sh \  
env-vars.sh \  
download-install-app.sh \  
/build/  
  
# Change to build directory  
WORKDIR /build  
  
# Compile application  
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \  
/build/setup.sh && \  
# Cleanup  
rm -rf /var/lib/apt/lists/* && \  
cd /build/epics-dev && \  
git clean -fdx  
  
# Change to root directory  
WORKDIR /  
  
# Expose default EPICS v3 ports  
EXPOSE 5064/udp  
EXPOSE 5064/tcp  
EXPOSE 5065/udp  
EXPOSE 5065/tcp  
# Expose default EPICS v4  
EXPOSE 5075/udp  
EXPOSE 5075/tcp  
EXPOSE 5076/udp  
EXPOSE 5076/tcp  

