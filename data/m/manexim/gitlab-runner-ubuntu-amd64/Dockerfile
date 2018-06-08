FROM ubuntu:17.04  
  
RUN \  
apt-get -qq update && \  
apt-get -qq -y install build-essential pkg-config curl unzip && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["bash"]

