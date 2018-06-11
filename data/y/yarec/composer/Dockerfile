FROM yarec/php:cli  
  
RUN apk --update add \  
wget \  
curl \  
git \  
&& \  
rm /var/cache/apk/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  
  
# Entry point  
CMD [composer]  

