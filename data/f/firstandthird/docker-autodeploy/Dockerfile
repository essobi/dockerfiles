FROM node:6-alpine  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories  
RUN apk add --update docker git bash curl  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-
init_1.1.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
EXPOSE 8080  
ENV HOME=/home/app  
WORKDIR $HOME/src  
  
COPY package.json $HOME/src/package.json  
RUN npm install --production  
  
COPY . $HOME/src  
  
CMD ["dumb-init", "npm", "start"]  

