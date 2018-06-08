FROM ubuntu:latest  
RUN apt-get update  
RUN apt-get install -y git  
  
MAINTAINER Aamir Latif <aamir@vendr.tech>  
  
FROM node:8  
# update npm to v5.1.0  
RUN rm -rf /usr/local/lib/node_modules/npm \  
&& mkdir /usr/local/lib/node_modules/npm \  
&& curl -sL https://github.com/npm/npm/archive/v5.1.0.tar.gz | tar xz -C
/usr/local/lib/node_modules/npm --strip-components=1 \  
&& npm --version  
  
RUN npm install sails -g  
  
RUN mkdir -p /service/app  
WORKDIR /service/app  
  
#FROM vendr/financials:latest  
COPY package.json /service/app  
#RUN export PATH="$HOME/usr/bin/git/bin:$PATH"  
RUN npm install --production  
  
COPY . /service/app  
  
EXPOSE 80  
CMD NODE_ENV=production sails lift

