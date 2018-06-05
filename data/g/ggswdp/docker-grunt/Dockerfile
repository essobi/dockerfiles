FROM debian:jessie  
MAINTAINER GGS Team WDP <wdp-php@goodgamestudios.com>  
  
RUN apt-get update && \  
apt-get install -y gcc ant ant-contrib libpng12-dev wget git bzip2 unzip curl
&& \  
apt-get clean  
  
WORKDIR /opt  
RUN wget http://nodejs.org/dist/v4.2.2/node-v4.2.2-linux-x64.tar.gz && \  
tar zxvf node-v4.2.2-linux-x64.tar.gz && \  
ln -s /opt/node-v4.2.2-linux-x64 /opt/node && \  
ln -s /opt/node/bin/node /usr/bin/node && \  
ln -s /opt/node/bin/npm /usr/bin/npm  
  
RUN npm install grunt-cli && \  
npm install node-sass && \  
ln -s /opt/node_modules/grunt-cli/bin/grunt /usr/bin/grunt && \  
ln -s /opt/node_modules/node-sass/bin/node-sass /usr/bin/node-sass  
  
ADD package.json /opt/  
RUN cd /opt && npm install  
  
RUN apt-get -y install nodejs-legacy && npm install -g galenframework-cli  
  
RUN groupadd --gid 503 jenkins ; \  
useradd -ms /bin/bash -g jenkins --uid 4211 jenkins  
RUN chown -R jenkins:jenkins /home/jenkins  
  
RUN curl -o /var/tmp/BrowserStackLocal.zip
https://www.browserstack.com/browserstack-local/BrowserStackLocal-
linux-x64.zip && \  
cd /opt && unzip /var/tmp/BrowserStackLocal.zip && \  
chown jenkins:jenkins /opt/BrowserStackLocal  
  
WORKDIR /home/jenkins

