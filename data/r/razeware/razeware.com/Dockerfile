FROM razeware/nginx:latest  
  
# Need to tidy up  
RUN rm -rf /var/cache/apk/* && \  
rm /etc/nginx/sites-enabled/default.conf  
  
# Add nginx config  
ADD ./etc/nginx/sites-enabled/razeware.conf /etc/nginx/sites-
enabled/razeware.conf  
  
# Add content  
RUN mkdir -p /var/www/razeware  
WORKDIR /var/www/razeware  
COPY ./public ./public  

