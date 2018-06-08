FROM alpine:3.6  
ENV APP_ROOT=/app  
RUN mkdir -p ${APP_ROOT}  
WORKDIR ${APP_ROOT}  
EXPOSE 80  
COPY apk-packages.txt ${APP_ROOT}/  
RUN apk add --no-cache $(grep -vE "^\s*#" ${APP_ROOT}/apk-packages.txt | tr
"\r\n" " ")  
  
COPY package.json yarn.lock ${APP_ROOT}/  
RUN yarn install && yarn cache clean  
  
COPY nginx-site.conf ${APP_ROOT}/  
RUN mkdir -p /run/nginx && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
ln -sf ${APP_ROOT}/nginx-site.conf /etc/nginx/conf.d/default.conf  
  
# Copies the rest of the app and builds it  
COPY . ${APP_ROOT}/  
RUN yarn ng build -- --target=production --environment=prod  
  
CMD ["nginx", "-g", "daemon off;"]  

