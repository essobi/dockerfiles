# Import nginx  
FROM nginx  
  
RUN mkdir -p /home/www/public_html/jonasknobloch.me/public  
RUN mkdir -p /home/www/public_html/jonasknobloch.me/public/img  
RUN mkdir -p /home/www/public_html/jonasknobloch.me/public/js  
  
# Copy static HTML / CSS / JS stuff  
COPY img/ /home/www/public_html/jonasknobloch.me/public/img  
COPY js/ /home/www/public_html/jonasknobloch.me/public/js  
COPY favicon.ico /home/www/public_html/jonasknobloch.me/public  
COPY index.html /home/www/public_html/jonasknobloch.me/public  
  
RUN ls /home/www/public_html/jonasknobloch.me/public  
  
# Create directory for private key  
RUN mkdir -p /etc/ssl/private  
  
# Copy nginx config  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN ls -l /etc/ssl/certs  
RUN ls -l /etc/ssl/private  
  
# Expose ports (HTTP / HTTPS)  
EXPOSE 80  
EXPOSE 443  

