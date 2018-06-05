FROM nginx:1.11.10-alpine  
  
RUN apk add --update \  
bash \  
&& rm -rf /var/cache/apk/*  
  
COPY build/nginx.conf /etc/nginx/nginx.conf  
COPY dist /usr/share/nginx/html/  
COPY scripts/write-global-variables.sh /opt/  
  
EXPOSE 80  
WORKDIR /opt  
ENTRYPOINT [ "/bin/sh", "-c", "./write-global-variables.sh
/usr/share/nginx/html/index.html && nginx -g 'daemon off;'" ]  

