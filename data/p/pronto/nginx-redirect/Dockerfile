FROM nginx  
  
EXPOSE 80  
ADD redirect.conf /etc/nginx/conf.d/redirect.template  
  
CMD /bin/sh -c 'envsubst "\$REDIRECT_TO_URL_PREFIX" <
/etc/nginx/conf.d/redirect.template > /etc/nginx/conf.d/default.conf && nginx
-g "daemon off;"'  

