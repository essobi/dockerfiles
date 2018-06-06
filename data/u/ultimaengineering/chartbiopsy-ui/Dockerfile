FROM node:alpine  
RUN apk update && apk add nginx && apk add bash  
RUN adduser -D -g 'www' www && mkdir /www && chown -R www:www /var/lib/nginx
&& chown -R www:www /www  
WORKDIR /app/webapp  
COPY "public" "/app/webapp/public/"  
COPY "src" "/app/webapp/src/"  
COPY "package.json" "/app/webapp/"  
# COPY fullchain.pem /etc/ssl/certs/  
# COPY privkey.pem /etc/ssl/certs/  
# COPY nginx.conf /etc/nginx/  
COPY SSLandAPP.conf /etc/nginx/conf.d/default.conf  
#RUN chmod 400 /etc/ssl/certs/fullchain.pem && chmod 400
/etc/ssl/certs/privkey.pem &&  
RUN mkdir -p /run/nginx  
RUN npm install && npm run build && cp -r /app/webapp/build/* /www/ && rm -rf
/app/webapp  
EXPOSE 80  
EXPOSE 443  
CMD nginx -g "daemon off;"

