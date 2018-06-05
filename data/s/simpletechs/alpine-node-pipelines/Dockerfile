FROM mhart/alpine-node:latest  
  
RUN apk update && \  
apk add bash git openssh-client curl make gcc g++ binutils-gold python linux-
headers paxctl libgcc libstdc++ git perl --no-cache && \  
npm install -g gulp karma nodemon yarn bower && \  
mkdir /root/.ssh && \  
ssh-keyscan github.com bitbucket.org >> /root/.ssh/known_hosts

