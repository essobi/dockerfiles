FROM node:alpine  
  
COPY package.json /cmhp/package.json  
COPY main.coffee /cmhp/main.coffee  
COPY logic.coffee /cmhp/logic.coffee  
  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache bash git openssh && \  
npm install -g gulp  
  
RUN cd /cmhp && \  
npm install  
  
EXPOSE 31337 31338  
WORKDIR /cmhp  
ENTRYPOINT ["node_modules/coffee-script/bin/coffee", "main.coffee"]  

