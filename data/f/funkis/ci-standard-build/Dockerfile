FROM node:8.2-alpine  
  
# Install npm 5.2 since 5.3 has a show stopping bug that prevents us from
running post scripts.  
RUN cd ~ && npm install npm@5.2 && rm -rf /usr/local/lib/node_modules && mv
node_modules /usr/local/lib/  
  
RUN apk update && apk upgrade \  
&& apk add \--no-cache bash git openssh rsync \  
&& npm install -g grunt-cli  

