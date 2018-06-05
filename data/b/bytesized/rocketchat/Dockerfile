FROM bytesized/debian-base  
ENV RC_VERSION latest  
  
MAINTAINER maran@bytesized-hosting.com  
  
# gpg: key 4FD08014: public key "Rocket.Chat Buildmaster
<buildmaster@rocket.chat>" imported  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
0E163286C20D07B9787EBE9FD7F9D0414FD08104  
  
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
  
ENV NODE_VERSION 0.10.45  
RUN set -x \  
&& apt-get update && apt-get install -y curl ca-certificates imagemagick --no-
install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm cache clear  
  
VOLUME /app/uploads  
  
RUN set -x \  
&& curl -SLf "https://rocket.chat/releases/${RC_VERSION}/download" -o
rocket.chat.tgz \  
&& curl -SLf "https://rocket.chat/releases/${RC_VERSION}/asc" -o
rocket.chat.tgz.asc \  
&& gpg --verify rocket.chat.tgz.asc \  
&& tar -zxf rocket.chat.tgz -C /app \  
&& rm rocket.chat.tgz rocket.chat.tgz.asc \  
&& cd /app/bundle/programs/server \  
&& npm install \  
&& npm cache clear  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.2 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt-get update && apt-get install -y mongodb-org  
  
VOLUME /database  
  
# needs a mongoinstance - defaults to container linking with alias 'mongo'  
ENV MONGO_URL=mongodb://127.0.0.1:27017/rocketchat \  
HOME=/tmp \  
PORT=3000 \  
ROOT_URL=http://localhost:3000 \  
Accounts_AvatarStorePath=/app/uploads \  
Accounts_AvatarStoreType=FileSystem  
  
  
EXPOSE 3000  
COPY static/ /  

