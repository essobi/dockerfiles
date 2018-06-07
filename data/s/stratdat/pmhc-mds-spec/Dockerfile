FROM nginx  
COPY build/html /usr/share/nginx/html  
# Put favicon where its expected  
COPY _static/favicon.ico /usr/share/nginx/html  
# Custom start script to enable 404 error page  
RUN mkdir /app  
ADD start_nginx.sh /app  
CMD /app/start_nginx.sh  

