FROM haskell:7.10  
MAINTAINER kirillseva "kirill.sevastyanenko@avant.com"  
RUN \  
# Update aptitude  
apt-get update && \  
# Install software dependencies  
apt-get install -y --force-yes \  
git \  
libpq-dev  
  
CMD ['bin/bash']  

