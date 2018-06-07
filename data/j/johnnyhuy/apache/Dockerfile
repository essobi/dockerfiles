FROM httpd:alpine  
  
LABEL com.johnnyhuy.version="1.0.0"  
LABEL com.johnnyhuy.author="Johnny Huynh"  
LABEL com.johnnyhuy.author-email="contact@johnnyhuy.com"  
LABEL com.johnnyhuy.release-date="2017-10-26"  
  
# Update existing packages  
RUN apk update && apk upgrade  
  
# Custom config to enable modules  
ADD ./config/httpd.conf /usr/local/apache2/conf/httpd.conf  
  
EXPOSE 80 443

