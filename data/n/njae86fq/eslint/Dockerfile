FROM debian:jessie  
  
ENV NVM_DIR=/opt/nvm \  
APP_DIR=/opt/app  
ENV
PATH=${APP_DIR}/node_modules/.bin:${NVM_DIR}/versions/node/default/bin:$PATH  
  
COPY package.json npm-shrinkwrap.json ${APP_DIR}/  
  
RUN apt-get update \  
&& GIT_DEPS=' \  
ca-certificates \  
curl \  
git \  
' \  
BUILD_DEPS=${GIT_DEPS} \  
NVM_VERSION=0.30.1 \  
NODE_VERSION=5.7.0 \  
&& apt-get install -y --no-install-recommends ${BUILD_DEPS} \  
&& curl
https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh |
bash \  
&& . ${NVM_DIR}/nvm.sh \  
&& nvm install ${NODE_VERSION} \  
&& ln -s ${NVM_DIR}/versions/node/v${NODE_VERSION}
${NVM_DIR}/versions/node/default \  
&& cd ${APP_DIR} \  
&& npm install -d \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["eslint"]  
CMD ["--help"]  

