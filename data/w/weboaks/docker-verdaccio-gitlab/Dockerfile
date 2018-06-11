FROM node:8-alpine  
  
ENV NODE_ENV production  
  
RUN apk add --quiet --no-cache --virtual .gyp \  
python \  
build-base \  
git \  
&& \  
npm config set registry http://registry.npmjs.org/ && \  
yarn global add verdaccio@2.7.4 && \  
yarn global add verdaccio-gitlab@latest && \  
yarn cache clean && \  
apk --quiet del .gyp && \  
mkdir -p /verdaccio/conf /verdaccio/storage && \  
chown -R node:node /verdaccio  
  
ADD
https://raw.githubusercontent.com/verdaccio/verdaccio/master/conf/docker.yaml
/verdaccio/conf/config.yaml  
  
USER node  
  
VOLUME ["/verdaccio/storage"]  
  
CMD ["verdaccio", "--config", "/verdaccio/conf/config.yaml", "--listen",
"http://0.0.0.0:4873"]  

