FROM node:7  
LABEL maintainer="gie.spaepen@rombit.be"  
  
RUN apt-get update && \  
apt-get -y install apt-transport-https curl && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install yarn && \  
mkdir /build && \  
cd /build &&\  
node -v && \  
npm -v  
  
WORKDIR /build  
  
ENTRYPOINT "/bin/bash"  
  

