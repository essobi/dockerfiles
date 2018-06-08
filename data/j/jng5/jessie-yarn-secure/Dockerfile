FROM debian:jessie-slim  
MAINTAINER Julie Ng <hello@julie.io>  
  
# Install packages not included in slim  
RUN apt-get update && \  
apt-get install --assume-yes sudo curl apt-transport-https  
  
# Install node  
# See https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-
linux-distributions  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - && \  
apt-get update && \  
sudo apt-get install -y nodejs  
  
# Configure Debian Package Repository & install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add \- &&
\  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install yarn  

