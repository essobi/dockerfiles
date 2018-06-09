FROM praekeltfoundation/vxsandbox  
MAINTAINER Praekelt Foundation <dev@praekeltfoundation.org>  
  
# Install nodejs dependencies  
COPY package.json /app/package.json  
WORKDIR /app  
RUN apt-get-install.sh npm && \  
npm install --production && \  
apt-get-purge.sh npm  
  
# Workaround for sandboxed application losing context - manually install the  
# *dependencies* globally.  
# See https://github.com/praekelt/vumi-sandbox/issues/15  
RUN mv ./node_modules /usr/local/lib/  
  
# Copy in the app Javascript  
COPY go-*.js /app/  

