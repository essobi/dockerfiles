FROM nginx:1.12.2-alpine  
  
# TZ: https://github.com/primait/board/issues/1631  
ENV TZ=:/etc/localtime  
  
# aws cli  
RUN apk -Uuv add python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm -rf /var/cache/apk/*  
  
COPY files/nginx.conf /etc/nginx/nginx.conf  
COPY files/mime.types /etc/nginx/mime.types  
COPY files/fastcgi_params /etc/nginx/fastcgi_params  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  

