FROM node:8.9.3  
  
MAINTAINER Abdullah Morgan <paapaabdullahm@gmail.com>  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends libsasl2-dev; \  
rm -rf /var/lib/apt/lists/*; \  
apt-get clean  

