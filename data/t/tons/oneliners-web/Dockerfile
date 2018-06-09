FROM node:alpine as builder  
WORKDIR /src  
ADD . /src  
RUN npm install && npm run build  
  
FROM nginx:alpine  
WORKDIR /usr/share/nginx/html  
COPY \--from=builder /src/dist .  
RUN apk --no-cache add gettext  
CMD target=$(ls static/js/app.*.js) && envsubst '$ONELINERS_API' < $target >
$target && nginx -g 'daemon off;'  

