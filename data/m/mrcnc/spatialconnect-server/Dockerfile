FROM nginx  
COPY ./public/ /usr/share/nginx/html  
COPY ./nginx-config/spatialconnect.conf /etc/nginx/conf.d/spatialconnect.conf  
COPY ./nginx-config/spatialconnect-tls.conf /  
COPY ./nginx-config/start.sh /  
CMD /start.sh  

