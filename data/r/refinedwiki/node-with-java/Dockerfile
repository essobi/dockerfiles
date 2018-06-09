FROM node:6-alpine  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
ENV HEROKU_DIR=/root/heroku  
ENV HEROKU_NODE_VERSION=8.1.4  
# Heroku CLI requires node v8.0+ and since there is no binary distributed for
Alpine we have to build it from source.  
# First install the dependencies we actually need  
RUN apk add -Uuv curl bash git openjdk7 python && \  
# Dependencies for building node and installing awscli  
apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
py-pip \  
# Install AWS CLI  
&& pip install awscli \  
&& cd ~ \  
# Download the Node source and build it  
&& curl -SLO
"https://nodejs.org/dist/v${HEROKU_NODE_VERSION}/node-v${HEROKU_NODE_VERSION}.tar.xz"
\  
&& tar -xf "node-v${HEROKU_NODE_VERSION}.tar.xz" \  
&& cd "node-v${HEROKU_NODE_VERSION}" \  
&& ./configure \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
# Install the build Node binary to a separate directory  
&& mkdir -p $HEROKU_DIR \  
&& make install DESTDIR="${HEROKU_DIR}"/node \  
&& mv "${HEROKU_DIR}"/node/usr/local/* "${HEROKU_DIR}"/node \  
&& rm -rf "${HEROKU_DIR}/node/usr" \  
&& apk --purge del .build-deps \  
&& cd .. \  
&& rm "node-v${HEROKU_NODE_VERSION}.tar.xz" \  
&& rm -rf "node-v${HEROKU_NODE_VERSION}" && \  
# Update npm  
cd ~ && \  
npm install npm@latest && \  
rm -rf /usr/local/lib/node_modules && \  
mv node_modules /usr/local/lib/ && \  
# Install the Heroku CLI  
npm i heroku-cli -g && \  
# Build our own script for running Heroku CLI to make sure it uses the
separate Node version  
echo "$HEROKU_DIR/node/bin/node /usr/local/lib/node_modules/heroku-
cli/bin/run.js \"\$@\"" > "$HEROKU_DIR"/run-heroku.sh && \  
chmod +x "$HEROKU_DIR"/run-heroku.sh && \  
rm /usr/local/bin/heroku && \  
ln -s "$HEROKU_DIR/run-heroku.sh" /usr/local/bin/heroku && \  
# Link up Java  
ln -fs "${JAVA_HOME}/bin/"* /usr/bin/ && \  
# Do cleanup  
npm cache clear --force && \  
rm -rf /var/cache/apk/* && \  
# Test all the Utilities  
aws --version && \  
heroku --version && \  
java -version && \  
node --version && \  
npm \--version  
  
ENTRYPOINT ["/bin/bash"]  
  

