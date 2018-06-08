#  
# NodeJS Dockerfile  
#  
# Base image  
FROM longieirl/base  
  
MAINTAINER jlongieirl@gmail.com  
  
ENV NODE_VERSION 0.10.38  
ENV NPM_VERSION 1.4.28  
ENV PHANTOM_JS_VERSION 1.9.7-linux-x86_64  
  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
# Install Node  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
# Configure Node  
RUN export PYTHON=/usr/bin/python && \  
node -v && \  
npm -v && \  
npm install -g grunt-cli && \  
npm install -g node-gyp --msvs_version=2012 && \  
npm install -g nodemon && \  
npm install -g node-inspector@'^0.9.2' && \  
npm install -g grunt-contrib && \  
npm config set python /usr/bin/python && \  
node-gyp clean  
  
VOLUME ["/app"]  
WORKDIR /app  
  
# Run the application  
CMD [ "node" ]

