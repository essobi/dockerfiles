FROM kaixhin/lasagne:latest  
  
MAINTAINER Mikael Manukyan <hi@mmanukyan.io>  
  
RUN apt-get install -y --force-yes \  
wget \  
unzip \  
git \  
curl  
  
# installing Node.js  
# (from https://github.com/nodejs/docker-
node/blob/9a4e5a31df1e7d1df8b3a2d74f23f340d5210ada/6.2/Dockerfile)  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 5.11.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
# instaling DMN dependencies  
RUN pip install \  
scikit-learn \  
flask \  
flask_restful  
  
RUN mkdir -p /usr/app  
  
WORKDIR /usr/app  
  
RUN git clone \--depth=1 https://github.com/YerevaNN/dmn-ui.git dmn-ui && \  
git clone \--depth=1 https://github.com/YerevaNN/Dynamic-memory-networks-in-
Theano dmn  
  
# building UI  
WORKDIR /usr/app/dmn-ui  
  
RUN npm install -g bower gulp && \  
npm install --unsafe-perm && bower install --allow-root && \  
gulp build && \  
mv dist ../dmn/server/ui  
  
WORKDIR /usr/app/dmn  
  
RUN chmod +x ./fetch_babi_data.sh && \  
./fetch_babi_data.sh && \  
chmod +x ./fetch_glove_data.sh && \  
./fetch_glove_data.sh  
  
WORKDIR /usr/app/dmn/server  
  
EXPOSE 5000  
# cleaning up  
RUN rm -rf /usr/app/dmn-ui  
  
CMD python api.py

