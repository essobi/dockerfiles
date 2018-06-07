FROM node:9-alpine  
MAINTAINER Niels van Doorn <n.van.doorn@outlook.com>  
  
RUN apk add --update curl bash tar gpgme \  
&& curl -o- -L https://yarnpkg.com/install.sh | bash \  
&& apk del curl bash tar gpgme  
  
RUN yarn global add gulp  

