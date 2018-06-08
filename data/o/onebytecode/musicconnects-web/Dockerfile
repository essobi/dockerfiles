FROM mhart/alpine-node:8.2  
# FROM mhart/alpine-node:6  
WORKDIR /src  
ADD . .  
  
# If you have native dependencies, you'll need extra tools  
# RUN apk add --no-cache make gcc g++ python  
# If you need npm, don't use a base tag  
RUN npm install  
  
EXPOSE 8080  
CMD ["npm", "run", "start"]  

