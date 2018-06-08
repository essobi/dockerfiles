FROM nginx:stable-alpine  
  
COPY \--from=hairyhenderson/gomplate:v2.2.0-slim /gomplate /usr/bin/gomplate  
COPY proxy.conf.template /proxy.conf.template  
COPY proxy.pac.template /proxy.pac.template  
COPY 163-uwp.json /usr/share/nginx/html/163-uwp.json  
COPY ipquery.txt /usr/share/nginx/html/163/ipquery.txt  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
EXPOSE 80  
CMD ["/docker-entrypoint.sh"]  

