FROM razeware/nginx:latest  
  
# Need to tidy up  
RUN rm -rf /var/cache/apk/* && \  
rm /etc/nginx/sites-enabled/default.conf  
  
# Add nginx config  
ADD ./etc/nginx/sites-enabled/math-ninja.conf /etc/nginx/sites-enabled/math-
ninja.conf  
  
# Add content  
RUN mkdir -p /var/www/math-ninja  
WORKDIR /var/www/math-ninja  
COPY ./public ./public  

