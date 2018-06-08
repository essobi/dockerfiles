FROM node:alpine as build-env  
COPY ./package.json /workspace/package.json  
COPY ./.babelrc /workspace/.babelrc  
COPY ./src /workspace/src  
WORKDIR /workspace  
RUN npm install  
RUN npx babel src -d build  
  
FROM node:alpine  
ENV NODE_ENV=production  
COPY \--from=build-env /workspace/build /app  
COPY \--from=build-env /workspace/package.json /app/package.json  
WORKDIR /app  
RUN npm install  
EXPOSE 3005  
VOLUME [ "/var/run/docker.sock" ]  
VOLUME [ "/configs" ]  
CMD ["node", "/app/index.js"]

