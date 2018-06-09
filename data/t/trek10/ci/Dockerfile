FROM amazonlinux:with-sources  
LABEL maintainer="Jared Short <jshort@trek10.com>"  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.9.4  
RUN yum update -y  
RUN yum install xz -y  
RUN yum install git -y  
RUN yum install python27-devel.x86_64 -y  
RUN yum groupinstall 'Development Tools' -y  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz"  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc"  
RUN gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc  
RUN grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c -  
RUN tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1  
RUN rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt  
RUN ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
############# Install serverless dependencies  
RUN \  
npm install -g serverless@1.23.0  
  
# Install aws dependencies  
RUN \  
yum install aws-cli -y  
  
RUN yum -y install zlib-devel openssl-devel  
  
# Install Python 3.6  
RUN curl -O https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz  
RUN tar xJf Python-3.6.0.tar.xz  
WORKDIR /Python-3.6.0  
RUN ./configure --enable-optimizations && make && make install  
WORKDIR /  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  

