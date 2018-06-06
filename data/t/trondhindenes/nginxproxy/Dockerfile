FROM nginx  
COPY ./proxy.conf /app/proxy.conf  
COPY ./nginx.conf /etc/nginx/nginx.conf  
RUN rm /etc/nginx/conf.d/default.conf  
CMD /bin/bash -c "envsubst < /app/proxy.conf > /etc/nginx/conf.d/proxy.conf &&
cat /etc/nginx/conf.d/proxy.conf && nginx -g 'daemon off;'"  

