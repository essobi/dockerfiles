FROM node:alpine  
  
ENV PORT 3000  
ENV MONGO_URI 'mongodb://client-db/Client'  
RUN mkdir -p /var/app/client-api  
  
WORKDIR /var/app/client-api  
  
COPY package.json ./  
COPY yarn.lock ./  
  
RUN yarn install --pure-lockfile --no-progress --prod --ignore-optional
--ignore-platform  
  
COPY app.js ./  
COPY app_api ./app_api  
COPY .babelrc ./.babelrc  
COPY bin ./bin  
  
EXPOSE 3000  
CMD yarn start  

