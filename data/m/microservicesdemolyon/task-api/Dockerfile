FROM node:9.4.0-alpine AS buildcontainer  
COPY . .  
RUN npm install && \  
npm run build && \  
rm -rf node_modules && \  
npm install --production  
  
FROM node:9.4.0-alpine  
COPY \--from=buildcontainer dist dist  
COPY \--from=buildcontainer node_modules node_modules  
COPY package.json .  
RUN apk add --no-cache dumb-init  
ENTRYPOINT [ "dumb-init" ]  
CMD [ "npm", "run", "serve" ]  
EXPOSE 4200

