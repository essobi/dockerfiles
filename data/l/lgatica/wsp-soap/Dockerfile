FROM mhart/alpine-
node:5@sha256:f8f781dcccef9740ada3ef1c76810a7a69555ddd81cb5af6890c4e1f2fcdbc2e  
  
MAINTAINER Leonardo Gatica <lgatica@protonmail.com>  
  
# NPM dependencies (cache)  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/  
  
ADD . /opt/app  
WORKDIR /opt/app  
RUN npm run build && npm prune --production  
  
EXPOSE 8000  
CMD ["npm", "run", "docker-start"]  

