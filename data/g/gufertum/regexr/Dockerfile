FROM mhart/alpine-node:latest  
  
# Dockerfile Maintainer  
MAINTAINER Thomas M. Schaedler "thomas@lambda.li"  
# Install dependencies  
RUN apk --no-cache add --virtual build-dependencies git ca-certificates \  
# Install python  
&& apk add \--no-cache make gcc g++ python \  
# Pull regexr source from own fork  
&& git clone https://github.com/gufertum/regexr.git /opt/regexr \  
&& cd /opt/regexr \  
# Install gulp  
&& npm install -g gulp \  
# Install npm depenencies  
&& npm install  
  
EXPOSE 8080  
WORKDIR /opt/regexr  
ENTRYPOINT ["gulp","build"]

