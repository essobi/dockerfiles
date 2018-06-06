FROM node:8-alpine  
  
ENV CI_HOME /usr/local/chip-in  
  
RUN apk --update add pcre-dev openssl-dev curl git  
RUN mkdir -p ${CI_HOME}/ \  
&& cd ${CI_HOME} \  
&& git clone https://github.com/chip-in/rn-contents-server.git rn-contents-
server \  
&& cd ${CI_HOME}/rn-contents-server \  
&& npm i \  
&& npm run cleanbuild  
  
WORKDIR ${CI_HOME}/rn-contents-server  
  
ENTRYPOINT ["npm", "start", "--"]  
  

