FROM node:9 as builder  
WORKDIR /app  
# Use a multi-stage build docker file to first create an environment to build  
# the react application. Note that only the last FROM will create the final
docker image  
COPY package.json package-lock.json README.md .env.production ./  
RUN npm install  
ENV NODE_ENV production  
# consider using a .dockerignore file here instead of explicitly copying
things  
COPY /scripts scripts  
COPY /src src  
COPY /public public  
RUN npm run build  
  
FROM kyma/docker-nginx  
LABEL maintainer="chad@medlor.com"  
COPY \--from=builder /app/build /var/www  
CMD 'nginx'

