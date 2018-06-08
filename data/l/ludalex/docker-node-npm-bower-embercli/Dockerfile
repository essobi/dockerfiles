FROM node:7.3  
MAINTAINER Luca D'Alessandro <ludalex@gmail.com>  
  
RUN apt-get update && apt-get install -y apt-transport-https python-dev
libssl-dev  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install --fix-missing && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends -qq yarn=0.18.1-1 zip python-pip &&
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN export PATH="$PATH:`yarn global bin`"  
  
RUN pip install awscli  
  
# RUN npm install -g ember-cli  
# RUN npm install -g bower  
# RUN npm install -g phantomjs-prebuilt  
  
RUN yarn global add ember-cli && yarn global add bower && yarn global add
phantomjs-prebuilt  

