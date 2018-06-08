FROM node:7.9.0  
LABEL version="1.0.0" name="Gravada"  
  
ENV HOME=/home/application  
ENV AWS_BUILD_KEY="AKIAIPWH2IBUPLAC4JEA"  
ENV AWS_BUILD_SECRET="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"  
WORKDIR $HOME/gameplan  
  
COPY package.json yarn.lock $HOME/gameplan/  
RUN npm i -g phantomjs@2.1.7  
RUN yarn global add gulp webpack  
RUN yarn --pure-lockfile && yarn install  
COPY . $HOME/gameplan  
RUN gulp production  
RUN BABEL_ENV=production webpack --config ./webpack/build-production.js  
  
EXPOSE 8001  
EXPOSE 27017  
# CMD ["node", "./src/server/bin/index.js"]  
CMD ["gulp", "production:node:start"]  
  

