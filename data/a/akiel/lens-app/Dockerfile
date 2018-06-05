FROM nginx:1.9.7  
RUN rm /usr/share/nginx/html/*  
COPY resources/public/css /usr/share/nginx/html/css  
COPY resources/public/fonts /usr/share/nginx/html/fonts  
ADD https://s3.eu-central-1.amazonaws.com/lens-app/hap/lens.js
/usr/share/nginx/html/js/  
RUN chmod 644 /usr/share/nginx/html/js/lens.js  
COPY resources/public/index.html /usr/share/nginx/html/  
  
COPY docker/add-md5sums.sh /  
RUN chmod +x /add-md5sums.sh  
RUN /add-md5sums.sh  
RUN rm /add-md5sums.sh  
  
COPY docker/nginx.conf /etc/nginx/  
COPY docker/start.sh /  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

