FROM node:8-alpine AS build  
  
WORKDIR /app  
  
RUN apk update && \  
apk add git python g++ make  
  
ADD package.json package-lock.json ./  
  
RUN npm install  
  
ADD . .  
  
FROM node:8-alpine AS deploy  
WORKDIR /app  
COPY \--from=build /app /app  
CMD ["./bin/deepstream"]  
  

