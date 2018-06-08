# See http://training.play-with-docker.com/node-zeit-pkg/  
FROM node:latest AS build  
  
RUN npm install -g pkg pkg-fetch  
ENV NODE node8  
ENV PLATFORM alpine  
ENV ARCH x64  
RUN /usr/local/bin/pkg-fetch ${NODE} ${PLATFORM} ${ARCH}  
  
RUN mkdir -p /usr/src/app/release  
WORKDIR /usr/src/app  
  
COPY package.json .  
COPY package-lock.json .  
RUN npm install  
COPY . /usr/src/app  
RUN npm run build:dist && pkg -t ${NODE}-${PLATFORM}-${ARCH} \--output runner
release/index.js  
  
FROM alpine:latest  
  
RUN mkdir -p /app/output  
WORKDIR /app  
ENV NODE_ENV=production  
  
RUN apk update && apk add --no-cache libstdc++ libgcc  
  
COPY \--from=build /usr/src/app/runner /app/runner  
  
CMD ["/app/runner"]  

