FROM centos:7  
MAINTAINER Semen Shestakov <shestakovsemen@gmail.com>  
  
RUN set -x;\  
yum update -y;\  
yum install -y \  
gcc gcc-c++ \  
java \  
tar bzip2 \  
which \  
;\  
yum clean all  
  
# nodejs  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 0.12.7  
ENV NODE_DOWNLOAD_URL
https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz  
ENV NODE_DOWNLOAD_SHA256
6a2b3077f293d17e2a1e6dba0297f761c9e981c255a2c82f329d4173acf9b9d5  
RUN set -x;\  
curl -SLo nodejs.tgz "$NODE_DOWNLOAD_URL";\  
echo "$NODE_DOWNLOAD_SHA256 *nodejs.tgz" | sha256sum -c -;\  
tar -xzf "nodejs.tgz" -C /usr/local \--strip-components=1;\  
rm "nodejs.tgz"  
  
RUN npm install --global plus.garden  
ENV NODE_PATH /usr/local/lib/node_modules/  
  
COPY entrypoint.sh /  
  
WORKDIR /app  
ENTRYPOINT ["/entrypoint.sh"]  

