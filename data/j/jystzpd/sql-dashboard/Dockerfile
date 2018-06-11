  
# ============== 0 - Build Client ===================  
FROM mhart/alpine-node:8.9  
  
WORKDIR /app  
COPY client .  
  
RUN yarn install && yarn build  
  
# ========= 1 - Build server node_modules ===========  
FROM mhart/alpine-node:8.9  
WORKDIR /app  
COPY package.json yarn.lock ./  
RUN yarn install --production  
  
  
# ======= Container build  
FROM mhart/alpine-node:base-8.9  
WORKDIR /app  
  
COPY \--from=0 /app/build ./client/build  
COPY \--from=1 /app .  
COPY ./server ./server  
  
ENV PORT 80  
ENV NODE_ENV production  
  
EXPOSE 80  
CMD ["node", "server/"]  

