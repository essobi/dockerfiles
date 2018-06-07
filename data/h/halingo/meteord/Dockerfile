FROM abernix/meteord:node-8-base  
  
RUN apt-get update && apt-get install -y \  
libcairo2-dev \  
libjpeg62-turbo-dev \  
libpango1.0-dev \  
libgif-dev \  
build-essential \  
g++  
  
ENV METEORD_DIR /opt/meteord  
COPY docker/dev/scripts $METEORD_DIR  
  
ENV NODE_MODULES_DIR /opt/nodejs/lib  
# use changes to package.json to force Docker not to use the cache  
# when we change our application's nodejs dependencies:  
COPY app/package.json $NODE_MODULES_DIR/package.json  
# Install PhantomJS separately because of error (TODO try fix)  
RUN cd $NODE_MODULES_DIR  
RUN npm install -g phantomjs@2.1.1 --unsafe-perm --production  
RUN npm install --production  
RUN rm $NODE_MODULES_DIR/package.json  
# RUN mkdir -p $METEORD_DIR && cp -a /tmp/node_modules $METEORD_DIR  
RUN bash $METEORD_DIR/lib/cleanup.sh

