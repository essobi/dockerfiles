FROM node:alpine  
  
MAINTAINER Sam Mousa <sam@mousa.nl>  
  
# We keep build-base since it is required for building node-sass.  
RUN apk add \--no-cache --update build-base python curl  
RUN mkdir -p /opt/yarn && \  
curl -L https://yarnpkg.com/latest.tar.gz | tar xzv -C /opt/yarn && \  
ln -s /opt/yarn/dist/bin/yarn /bin/yarn  
RUN yarn global add @angular/cli

