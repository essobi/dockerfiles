FROM node:boron-slim  
  
MAINTAINER dan78uk  
  
ENV BUILD_PACKAGES="build-essential unzip curl libaio1 python-minimal git
libfontconfig yarn wget tar"  
ENV NODE_LIBS="node-gyp nsp"  
ENV SCANNER_SOURCE_URL=https://github.com/UKHomeOffice/repo-security-
scanner/releases/download/0.3.1/  
ENV SCANNER_SOURCEFILE_NAME=scanrepo-0.3.1-linux-amd64.tar.gz  
  
RUN \  
curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y $BUILD_PACKAGES && \  
AUTO_ADDED_PACKAGES=`apt-mark showauto` && \  
rm -rf /var/lib/apt/lists/* && \  
wget ${SCANNER_SOURCE_URL}${SCANNER_SOURCEFILE_NAME} && \  
tar -zxvf ${SCANNER_SOURCEFILE_NAME} && \  
chmod +X ./scanrepo && \  
mv scanrepo /usr/bin/scanrepo  
  
RUN \  
npm install -g $NODE_LIBS  
  
WORKDIR /app  
  
CMD [ "node" ]  

