FROM nginx:stable-alpine  
  
RUN runtimeDeps='inotify-tools bash openssl' \  
&& apk update && apk upgrade && apk add $runtimeDeps  
  
COPY nginx.conf *.model /etc/nginx/  
  
VOLUME /etc/nginx/dhparam  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

