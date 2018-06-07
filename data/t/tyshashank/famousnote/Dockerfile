FROM microsoft/dotnet:1.1.0-sdk-projectjson  
  
MAINTAINER Shashank Tiwary  
  
ENV DOTNET_USE_POLLING_FILE_WATCHER=1  
ENV ASPNETCORE_URLS=http://*:5000  
COPY ./project.json /var/www/famousNote/project.json  
COPY ./package.json /var/www/famousNote/package.json  
COPY . /var/www/famousNote  
  
WORKDIR /var/www/famousNote  
  
# Install required packages  
RUN apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
ca-certificates \  
apt-transport-https \  
git \  
curl \  
wget \  
bzip2 \  
jq  
  
ENV HOME /root  
  
# install npm  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
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
  
ENV NPM_CONFIG_LOGLEVEL error  
ENV NODE_VERSION 6.7.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz"  
  
RUN cd /tmp && wget https://www.npmjs.org/install.sh && sh install.sh  
  
RUN npm install  
  
RUN npm run tsc  
  
RUN dotnet restore  
  
RUN dotnet build  
  
EXPOSE 5000  
ENTRYPOINT ["dotnet", "run"]

