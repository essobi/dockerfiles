FROM node:8-alpine  
ENV NPM_CONFIG_PREFIX="/.npm-global"  
ENV PATH="${NPM_CONFIG_PREFIX}/bin:${PATH}"  
ADD . /  
RUN apk add \--no-cache git openssh-client && \  
npm install @angular/cli@1.7.4 -g --unsafe-perm && \  
git config \--global user.email "continuous-deployment@converting.network" &&
\  
git config \--global user.name "Continuous deployment"  

