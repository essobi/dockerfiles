FROM node:8.11.1  
LABEL Author="Upstage Support <support@upstaged.tv>"  
  
ENV YARN_VERSION 1.6.0  
# installing specific version of yarn
https://github.com/yarnpkg/yarn/issues/1839  
# remove /usr/local/bin version which is installed by node base image  
# new yarn location is /usr/bin  
RUN apt-get update -qq && apt-get -y install apt-transport-https \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y -qq yarn=$YARN_VERSION-1 \  
&& rm /usr/local/bin/yarn*  
  
RUN npm install -g firebase-tools@3.18.2  

