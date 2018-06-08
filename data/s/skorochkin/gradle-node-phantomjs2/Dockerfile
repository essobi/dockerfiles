FROM skorochkin/java-gradle:latest  
  
ENV NODE_VERSION="0.12" \  
# hotfix for ultra slow npm install on Ubuntu  
NPM_CONFIG_REGISTRY="http://registry.npmjs.org/" \  
PHANTOMJS_VERSION=2.1.1-linux-x86_64 \  
PHANTOMJS_BIN=/usr/local/bin/phantomjs  
  
# install required packages  
RUN apt-get update -qq && apt-get -y -qq --no-install-recommends install \  
build-essential time \  
python python-dev python-pip \  
libwebp5 libfontconfig1 libjpeg8 libicu52  
  
RUN curl --silent --location https://deb.nodesource.com/setup_${NODE_VERSION}
| bash - && \  
apt-get -y install nodejs && npm cache clean && \  
npm install -g --no-optional npm bower && \  
npm install -g --no-optional build npm-cache gulp  
  
RUN wget -qO- -O /tmp/phantomjs.tbz
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}.tar.bz2
&& \  
tar xf /tmp/phantomjs.tbz -C /tmp && \  
mv /tmp/phantomjs-${PHANTOMJS_VERSION}/bin/phantomjs /usr/local/bin/phantomjs  
  
RUN pip -q install ansible==1.9.4  
  
# cleanup  
RUN rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && apt-get clean  
  
CMD []  

