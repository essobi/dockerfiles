FROM buildpack-deps:jessie  
  
# You start off as the 'strongloop' user.  
# If a RUN command needs root, you can use sudo  
# In addition to standard Linux commands you also have access to node, npm,  
# and slc commands  
# It is common to copy your current  
# DANGEROUS: this is a dev convenience container, everyone has sudo access  
RUN DEBIAN_FRONTEND=noninteractive sh -c '( \  
apt-get update -q && \  
apt-get install -y -q curl git wget lynx vim man-db ssh bash-completion sudo
apt-utils && \  
apt-get clean && apt-get autoclean)' > /dev/null && \  
useradd -ms /bin/bash dd && \  
chown -R dd /usr/local && \  
echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# gpg keys listed at https://github.com/nodejs/node  
#RUN set -ex \  
# && for key in \  
# 9554F04D7259F04124DE6B476D5A82AC7E37093B \  
# 94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
# 0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
# FD3A5288F042B6850C66B31F09FE44734EB7990E \  
# 71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
# DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
# B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
# C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
# B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
# ; do \  
# gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
# done  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.9.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
# && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
# && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
# && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
# && rm SHASUMS256.txt.asc SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# install global npm dependencies  
RUN echo "Installing global npm dependencies"  
RUN npm install -g strongloop  
RUN npm install -g gulp-cli  
RUN npm install -g loopback  
RUN npm install -g loopback-datasource-juggler  
RUN npm install -g babel-preset-es2015  
RUN npm install -g babel-loader  
RUN npm install -g babel-cli  
  
# add user 'hdbg'  
RUN echo "Adding user applicationserver"  
RUN useradd -ms /bin/bash -G sudo hdbg  
  
# copy npm's package.json  
COPY package.json /home/applicationserver  
#CMD cd /home/applicationserver  
# install dependencies  
RUN echo "Installing local npm dependencies"  
RUN cd /home/applicationserver && sudo npm install  
  
# copy source files  
COPY . /home/applicationserver  
ENV NODE_ENV development  
WORKDIR /home/applicationserver  
  
# run web server  
CMD ["npm", "run", "start-server"]  

