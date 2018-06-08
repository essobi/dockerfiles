FROM node:carbon as build-deps  
WORKDIR /app  
COPY ["package.json", "yarn.lock", "./"]  
RUN yarn install --silent  
  
FROM node:carbon-alpine as prod-deps  
ENV NODE_ENV production  
WORKDIR /app  
COPY ["package.json", "yarn.lock", "./"]  
RUN yarn install --silent  
  
FROM build-deps as build  
COPY . .  
RUN yarn build --silent  
  
FROM prod-deps as prod  
COPY \--from=build /app/dist/ /app/dist  
EXPOSE 8080  
CMD ["node", "dist/server"]  

