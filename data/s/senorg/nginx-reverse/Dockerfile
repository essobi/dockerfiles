FROM nginx  
COPY nginx.conf /etc/nginx/conf.d/reverse.template  
  
ENV BACKEND_HOST backend:8000  
ENV STATIC_PATH /srv/static  
ENV STATIC_URL /static/  
  
EXPOSE 80  
CMD /bin/bash -c 'envsubst "\$BACKEND_HOST \$STATIC_ROOT \$STATIC_URL" <
/etc/nginx/conf.d/reverse.template > /etc/nginx/conf.d/default.conf && nginx
-g "daemon off;"'  

