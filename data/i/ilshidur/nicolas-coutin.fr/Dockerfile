FROM mhart/alpine-node:8.5.0  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json yarn.lock ./  
RUN yarn  
  
COPY client client  
RUN (cd client && yarn && yarn build && rm -rf src)  
  
COPY server server  
RUN (cd server && yarn)  
  
ENV NODE_ENV production  
ENV PORT 3000  
  
CMD ["node", "server/app.js"]  
  
EXPOSE 3000  

