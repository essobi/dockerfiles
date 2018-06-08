FROM nginx:1.9.3  
COPY errors /errors  
RUN gzip -c9 /errors/error.html > /errors/error.html.gz  
RUN gzip -c9 /errors/maintenance.html > /errors/maintenance.html.gz  
RUN gzip -c9 /errors/notfound.html > /errors/notfound.html.gz  
COPY nginx.conf /etc/nginx/nginx.conf  

