FROM jc21/appserver  
  
# ENV VERSION=v0.10.40 CFLAGS="-D__USE_MISC"  
ENV VERSION=v0.12.7  
# ENV VERSION=v4.2.1  
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
apk del make gcc g++ python linux-headers paxctl ${DEL_PKGS} && \  
rm -rf /node-${VERSION} ${RM_DIRS} \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
RUN apk add --update groff python python-dev py-pip build-base git && pip
install virtualenv awscli && rm -rf /var/cache/apk/*  
RUN pip install --upgrade pip  
  
RUN npm install -g gulp bower  
RUN curl --insecure -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
  
WORKDIR /var/app  
  

