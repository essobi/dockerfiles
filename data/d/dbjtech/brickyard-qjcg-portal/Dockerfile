FROM dbjtech/brickyard-cli:build-essential as build-stage  
  
COPY ./brickyard_modules /brickyard-app/brickyard_modules  
  
WORKDIR /brickyard-app/  
  
RUN brickyard ls qjcg-portal && brickyard build qjcg-portal -vv  
  
FROM nginx:alpine  
  
RUN apk add tzdata --update --no-cache && cp /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && echo "Asia/Shanghai" /etc/localtime && apk del tzdata  
  
COPY \--from=build-stage ./brickyard-app/output/www /usr/share/nginx/html  
  
VOLUME /usr/share/nginx/html  
  
EXPOSE 80  

