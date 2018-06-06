FROM openjdk:alpine  
  
RUN apk --update --no-cache add php7 php7-json php7-phar php7-openssl
php7-ctype php7-mbstring php7-pdo_sqlite php7-tokenizer php7-xml php7-zlib
curl  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN apk --update --no-cache add nodejs  
  
RUN apk --update --no-cache add git openssh-client  
RUN mkdir ~/.ssh && \  
chmod 700 ~/.ssh && \  
touch ~/.ssh\known_hosts && \  
ssh-keyscan github.com >> ~/.ssh/known_hosts && \  
chmod 600 ~/.ssh\known_hosts  
  
ADD script.sh /script.sh  
RUN chmod 755 /script.sh  
  
ENTRYPOINT ["/script.sh"]  

