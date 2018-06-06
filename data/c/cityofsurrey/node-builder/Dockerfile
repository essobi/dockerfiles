FROM node:10.0.0-alpine  
  
# Add Docker repository  
RUN echo http://dl-6.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories  
  
# Install development packages  
RUN apk add --no-cache --update bash curl git openssh docker && \  
rm -rf /var/cache/apk/*  
  
# Install Node.js packages  
RUN yarn global add \  
conventional-github-releaser@1.1.10 --ignore-engines \  
snyk \  
landscape-node \  
bunyan  

