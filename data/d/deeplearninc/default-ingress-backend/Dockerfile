FROM nginx:1.13-alpine  
  
LABEL vendor="DeepLearn Inc"  
  
COPY templates/nginx.conf /etc/nginx/  
COPY templates/default.conf.template /etc/nginx/conf.d/  
  
CMD /bin/sh -c "envsubst < /etc/nginx/conf.d/default.conf.template >
/etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"  

