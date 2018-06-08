FROM node:9.5.0-alpine as build  
  
ADD . /  
RUN apk add --update yarn \  
&& yarn install  
  
FROM node:9.5.0-alpine  
  
ADD src /pstd  
COPY \--from=build /node_modules /node_modules  
  
ENTRYPOINT ["node", "/pstd/app.js"]

