FROM node:8.9-alpine as node-webpack-eslint-stylelint  
  
LABEL authors="Leo Caseiro"  
  
#Linux setup  
RUN apk update \  
&& apk add --update alpine-sdk \  
&& apk del alpine-sdk \  
&& rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \  
&& npm cache verify \  
&& sed -i -e "s/bin\/ash/bin\/sh/" /etc/passwd  
  
# Install npm global packages  
RUN npm install -g webpack eslint stylelint  

