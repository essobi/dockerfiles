FROM node:6  
MAINTAINER Jonas Su <jonas@25sprout.com>  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list \  
&& apt-get -qq update \  
&& apt-get -qqy upgrade \  
&& apt-get install -qqy yarn openssh-client \  
&& apt-get clean \  
&& rm -rf /usr/local/bin/yarn*  
  
RUN apt-get -qq update \  
&& apt-get -qqy upgrade \  
&& apt-get install -qqy awscli \  
&& apt-get clean  
  
RUN apt-get -qq update \  
&& apt-get -qqy upgrade \  
&& apt-get install -qqy curl jq \  
&& apt-get clean  
  
RUN npm install -g ajv-cli  
  
RUN apt-get -qq update \  
&& apt-get -qqy upgrade \  
&& apt-get install -qqy rsync \  
&& apt-get clean  
  
RUN apt-get -qq update \  
&& apt-get -qqy upgrade \  
&& apt-get install -qqy zip unzip \  
&& apt-get clean  

