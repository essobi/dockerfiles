FROM node:8-alpine AS build  
  
ADD . /build  
  
WORKDIR /build  
  
RUN apk update && apk add python make g++ && \  
npm install -g yarn && \  
yarn install && \  
yarn run test && \  
yarn run tsc && \  
rm -rf node_modules/ && \  
yarn install --production=true  
  
FROM node:8-alpine AS runtime  
  
COPY \--from=build /build /app  
  
WORKDIR /app  
  
ENV PORT 8080  
ENV DBURL http://localhost:5894  
ENV DEBUG mqtt-http-gateway:*  
  
CMD node dist  

