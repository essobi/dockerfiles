FROM thredup/node:6.11.3-debian  
  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
g++ \  
gcc \  
git \  
make \  
nasm \  
python \  
zlib1g-dev \  
&& yarn global add npm@5.4.1 \  
&& rm -R /var/lib/apt/lists/*  
  
ONBUILD ARG NPM_TOKEN  
  
ONBUILD ARG NODE_ENV=production  
ONBUILD ENV NODE_ENV=${NODE_ENV}  
  
ONBUILD ARG NPM_LOG_LEVEL=error  
ONBUILD ENV npm_config_loglevel=${NPM_LOG_LEVEL}  
  
ONBUILD ARG PUBLISH_ASSETS=false  
ONBUILD ENV PUBLISH_ASSETS=${PUBLISH_ASSETS}  
ONBUILD ARG AWS_KEY  
ONBUILD ENV AWS_KEY=${AWS_KEY}  
ONBUILD ARG AWS_SECRET  
ONBUILD ENV AWS_SECRET=${AWS_SECRET}  
ONBUILD ARG REVISION  
ONBUILD ENV REVISION=${REVISION}  
  
ONBUILD COPY package.json npm-shrinkwrap.json ./  
ONBUILD RUN echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" >> ~/.npmrc \  
&& npm install \  
&& rm ~/.npmrc  
ONBUILD COPY . ./  
ONBUILD RUN if [ -f ./scripts/build.sh ]; then ./scripts/build.sh; fi  

