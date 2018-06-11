FROM node:8-alpine  
  
###Update packages###  
RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& echo "@edgecommunity http://dl-cdn.alpinelinux.org/alpine/edge/community"
>> /etc/apk/repositories \  
&& apk update \  
&& apk upgrade \  
&& apk add \--upgrade apk-tools@edge \  
&& npm install npm@latest -g && apk add \--update openssl \  
###Install new packages###  
#yarn (remove current one)  
&& rm /usr/local/bin/yarn && rm /usr/local/bin/yarnpkg \  
&& apk add yarn@edgecommunity --update-cache --allow-untrusted \  
#zip  
&& apk add zip \  
#Parallel  
&& apk add parallel \  
#AWS cli  
&& apk add py-pip && python -m pip install --upgrade pip \  
&& pip install awscli && aws configure set default.region us-west-2 \  
#AWS sam-local  
&& pip install aws-sam-cli  

