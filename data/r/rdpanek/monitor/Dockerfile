# VERSION 0.5.1  
FROM node:7-alpine  
MAINTAINER Radim Daniel Pánek <rdpanek@gmail.com>  
  
# main env  
ENV APP_DIR /opt/monitor  
  
# Create app directory  
RUN mkdir -p ${APP_DIR}  
WORKDIR ${APP_DIR}  
COPY . ${APP_DIR}  
  
RUN apk add --no-cache --virtual .yarn-deps curl gnupg tar && \  
echo 'export PATH="$HOME/.yarn/bin:$PATH"' > ~/.bashrc && \  
curl -o- -L https://yarnpkg.com/install.sh | sh && \  
ln -s ~/.yarn/bin/yarn /bin/yarn && \  
yarn install && yarn build && \  
apk del .yarn-deps tar curl gnupg  
  
CMD ["yarn","start"]  

