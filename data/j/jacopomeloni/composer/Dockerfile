FROM php:7.2-cli-alpine  
  
LABEL MANTAINER=jacopomeloni@gmail.com  
  
# install packages  
RUN docker-php-ext-install pcntl  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer\  
&& composer global require hirak/prestissimo  
  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set up the command arguments  
CMD ["-"]  
ENTRYPOINT ["composer", "--ansi"]

