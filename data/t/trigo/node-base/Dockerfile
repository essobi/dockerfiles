# ----* Dependencies *---  
FROM node:9.11.1-slim AS dependencies  
  
RUN apt-get update -yqq && apt-get install -yqq git  
  
ONBUILD ARG NPM_TOKEN  
ADD npmrc /root/.npmrc  
  
WORKDIR /app  
  
ONBUILD ADD package.json .  
ONBUILD ADD yarn.lock .  
  
ONBUILD RUN yarn install --no-cache --frozen-lockfile --production  
ONBUILD RUN cp -R node_modules node_modules_prod  
  
ONBUILD ADD . /app  
  
ONBUILD RUN rm /root/.npmrc  

