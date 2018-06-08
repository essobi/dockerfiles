FROM node:8.10.0-alpine  
  
COPY . /app/  
  
WORKDIR /app  
  
RUN apk add --no-cache -t build-deps build-base git python \  
&& yarn --pure-lockfile \  
&& apk del --purge build-deps  
  
EXPOSE 8080  
CMD ["tsc | node ./gitignore-tsc-emitted-files.js"]  

