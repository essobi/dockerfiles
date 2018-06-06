FROM node:9.2.0  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-
init_1.1.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY package.json /app/  
RUN yarn install --production  
COPY . /app  
  
RUN mv ./config/stage.js ./config/index.js  
RUN mv ./config/server-config-stage.js ./config/server-config.js  
RUN yarn next-build  
  
EXPOSE 80  
# RUN groupadd -r nodejs && useradd -m -r -g nodejs nodejs  
# USER nodejs  
CMD [ "dumb-init", "node", "server.js" ]

