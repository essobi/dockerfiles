FROM node:9-alpine  
RUN mkdir -p /app  
WORKDIR /app  
ENV NODE_PATH src/  
ENV REACT_APP_API_URL ${REACT_APP_API_URL}  
ENV REACT_APP_SENTRY ${REACT_APP_SENTRY}  
COPY package.json yarn.lock ./  
RUN yarn install  
COPY . .  
RUN yarn build  
  
FROM zzswang/docker-nginx-react:latest  
ENV DEBUG=off  
COPY \--from=0 /app/build/ /app  

