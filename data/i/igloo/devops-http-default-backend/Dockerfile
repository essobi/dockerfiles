FROM node:9.2.0-alpine  
ENV NODE_ENV production  
ENV NPM_CONFIG_LOGLEVEL warn  
WORKDIR /app  
COPY ./package.json ./package-lock.json ./gatsby-config.js ./  
RUN npm install  
COPY ./gatsby-config.js ./  
COPY ./src ./src/  
RUN npm run build  
  
FROM nginx:1.13.3-alpine  
COPY ./nginx-server.conf /etc/nginx/conf.d/default.conf  
COPY \--from=0 /app/public /public  
RUN mkdir /public/__default_backend_files && \  
mv /public/static /public/__default_backend_files/static && \  
find /public -type f ! -path "*/index.html" ! -path "*/static/*" -exec mv {}
/public/__default_backend_files/ \;  

