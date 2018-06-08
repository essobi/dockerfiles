FROM raseel/ubuntu-trusty  
  
MAINTAINER Raseel Bhagat <raseelbhagat@gmail.com>  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
ca-certificates npm 'ruby-full'  
RUN mkdir /nodejs && curl
https://nodejs.org/dist/v0.10.40/node-v0.10.40-linux-x64.tar.gz | tar xvzf -
-C /nodejs --strip-components=1  
RUN npm install grunt grunt-cli bower forever pm2 -g  
ENV PATH $PATH:/nodejs/bin  

