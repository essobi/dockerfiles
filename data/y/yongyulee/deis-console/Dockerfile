#  
# Deis Console Dockerfile  
#  
# https://github.com/yongyu-lee/deis-console  
#  
# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Yongyu Lee <aleeyyu@gmail.com>  
  
# Install.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y && \  
apt-get install -y curl git unzip vim wget  
  
RUN \  
curl -sSL http://deis.io/deis-cli/install.sh | sh -s 1.4.1 && \  
mv ./deis /usr/local/bin && \  
echo "Installed deis to /usr/local/bin"  
  
RUN \  
curl -sSL http://deis.io/deisctl/install.sh | sh -s 1.4.1 && \  
mv ./deisctl /usr/local/bin && \  
echo "Installed deisctl to /usr/local/bin"  
  
RUN \  
wget
https://github.com/coreos/fleet/releases/download/v0.9.0/fleet-v0.9.0-linux-
amd64.tar.gz && \  
tar -zxvf fleet-v0.9.0-linux-amd64.tar.gz && \  
mv fleet-v0.9.0-linux-amd64/fleetctl /usr/local/bin && \  
rm -rf fleet-v0.9.0-linux-amd64.tar.gz fleet-v0.9.0-linux-amd64 && \  
echo "Installed fleetctl to /usr/local/bin"  
  
# Enable `ssh-add`  
RUN echo 'eval `ssh-agent -s`' >> ~/.bashrc  
  
# Create a mount point  
VOLUME [ "/root/private_keys" ]  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD [ "bash" ]  

