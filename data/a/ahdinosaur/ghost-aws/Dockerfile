FROM ghost:0.11.0  
MAINTAINER Michael Williams <michael.williams@enspiral.com>  
  
RUN \  
apt-get update && apt-get install -y git --no-install-recommends && rm -rf
/var/lib/apt/lists/* && \  
npm install --production ahdinosaur/ghost-s3-storage-adapter#does-not-inherit-
bug && \  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
-o APT::AutoRemove::SuggestsImportant=false git && \  
mkdir -p $GHOST_CONTENT/storage && \  
mv node_modules/ghost-s3-storage-adapter
$GHOST_SOURCE/core/server/storage/ghost-s3 && \  
npm cache clean && \  
rm -rf /tmp/npm* && \  
ln -s $(pwd) $(pwd)/node_modules/ghost  
  
COPY config.js $GHOST_CONTENT  

