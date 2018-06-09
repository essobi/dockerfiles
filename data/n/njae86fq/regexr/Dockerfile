FROM debian:jessie  
  
ENV NVM_DIR=/opt/nvm \  
APP_DIR=/opt/app  
ENV PATH=${APP_DIR}/node_modules/.bin:${NVM_DIR}/default/bin:$PATH  
  
COPY npm-shrinkwrap.json /tmp/  
  
RUN apt-get update \  
&& GIT_DEPS=' \  
ca-certificates \  
git \  
' \  
OTHER_DEPS=' \  
curl \  
' \  
BUILD_DEPS="${GIT_DEPS} ${OTHER_DEPS}" \  
NVM_VERSION=0.30.1 \  
NODE_VERSION=5.7.0 \  
REGEXR_COMMIT_ID=a0db58d335b94f763896a74589a7ae2f2390439c \  
&& apt-get install -y --no-install-recommends ${BUILD_DEPS} \  
&& curl
https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh |
bash \  
&& . ${NVM_DIR}/nvm.sh \  
&& nvm install ${NODE_VERSION} \  
&& ln -s ${NVM_DIR}/v${NODE_VERSION} ${NVM_DIR}/default \  
&& npm config set unsafe-perm true \  
&& git clone https://github.com/gskinner/regexr ${APP_DIR} \  
&& cd ${APP_DIR} \  
&& git checkout ${REGEXR_COMMIT_ID} \  
&& npm install -g gulp \  
&& mv /tmp/npm-shrinkwrap.json ${APP_DIR} \  
&& npm install -d \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR ${APP_DIR}  
EXPOSE 8080  
ENTRYPOINT ["sh", "-c", ". ${NVM_DIR}/nvm.sh && nvm use stable && gulp build"]  

