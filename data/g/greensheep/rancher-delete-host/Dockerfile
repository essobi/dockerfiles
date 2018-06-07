# Use alpine linux as the base and install  
# node js. See: https://github.com/mhart/alpine-node  
FROM alpine:3.2  
# Install node  
ENV VERSION=v4.2.1  
RUN apk add --update curl make gcc g++ python linux-headers paxctl libgcc
libstdc++ && \  
curl -sSL https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.gz | tar -xz
&& \  
cd /node-${VERSION} && \  
./configure --prefix=/usr ${CONFIG_FLAGS} && \  
make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make install && \  
paxctl -cm /usr/bin/node && \  
cd / && \  
if [ -x /usr/bin/npm ]; then \  
npm install -g npm@2 && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf; \  
fi && \  
apk del curl make gcc g++ python linux-headers paxctl ${DEL_PKGS} && \  
rm -rf /etc/ssl /node-${VERSION} ${RM_DIRS} \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
# Install app packages  
RUN mkdir -p /src/app  
COPY ./package.json /src/  
WORKDIR /src  
RUN npm install  
  
# Install app  
COPY . /src/app  
  
# Set default dir, port and cmd  
WORKDIR /src/app  
EXPOSE 9090  
CMD ["npm", "start"]  

