FROM jedisct1/phusion-baseimage-latest:16.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN (curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -)
&& \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
(curl -sL https://deb.nodesource.com/setup_8.x | bash -) && \  
apt-get install --no-install-recommends -yq nodejs yarn python build-essential
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
yarn global add node-gyp  
  
COPY package.json /tmp/package.json  
RUN cd /tmp && yarn && \  
mkdir -p /usr/app && \  
mv /tmp/node_modules /usr/app/  
  
COPY package.json README.md .babelrc server.js /usr/app/  
COPY tasks /usr/app/tasks/  
  
RUN mkdir /etc/service/express  
COPY bin/express.run.sh /etc/service/express/run  
  
EXPOSE 80  
WORKDIR /usr/app/  

