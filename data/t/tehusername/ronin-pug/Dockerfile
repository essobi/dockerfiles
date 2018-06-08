FROM mhart/alpine-node:8  
WORKDIR /src  
ENV NODE_ENV production  
COPY package.json yarn.lock ./  
RUN yarn --pure-lockfile  
  
COPY . .  
  
EXPOSE 3000  
CMD ["node", "./bin/www"]  

