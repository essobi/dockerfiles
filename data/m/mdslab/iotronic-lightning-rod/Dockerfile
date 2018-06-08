FROM node:carbon-slim  
  
RUN apt-get update && apt-get install -y \  
socat dsniff fuse libfuse-dev git ntpdate python pkg-config build-essential \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN npm install -g --unsafe gyp autobahn nconf @mdslab/wstun fuse-bindings
requestify is-running connection-tester log4js@1.1.1 q fs-access mknod
jsonfile \  
&& npm install -g --unsafe https://github.com/PlayNetwork/node-
statvfs/tarball/v3.0.0 \  
&& npm cache --force clean  
  
RUN mkdir -p /var/lib/iotronic/plugins \  
&& mkdir -p /var/lib/iotronic/drivers/mountpoints/ \  
&& mkdir -p /var/log/iotronic/ \  
&& touch /var/log/iotronic/lightning-rod.log  
  
WORKDIR /usr/local/lib/node_modules/  
  
RUN git clone --depth=1 git://github.com/MDSLab/s4t-lightning-rod.git
./@mdslab/iotronic-lightning-rod  
  
ENV NODE_PATH=/usr/local/lib/node_modules  
ENV IOTRONIC_HOME=/var/lib/iotronic  
ENV LIGHTNINGROD_HOME=/usr/local/lib/node_modules/@mdslab/iotronic-lightning-
rod  
  
RUN cp /usr/local/lib/node_modules/@mdslab/iotronic-lightning-
rod/modules/plugins-manager/plugins.example.json
/var/lib/iotronic/plugins/plugins.json \  
&& cp /usr/local/lib/node_modules/@mdslab/iotronic-lightning-
rod/modules/drivers-manager/drivers.example.json
/var/lib/iotronic/drivers/drivers.json  
  
WORKDIR /usr/local/lib/node_modules/@mdslab/iotronic-lightning-rod/  
  
VOLUME /var/lib/iotronic  
  
CMD [ "node", "lightning-rod"]  
  

