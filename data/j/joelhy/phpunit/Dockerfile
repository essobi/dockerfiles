FROM joelhy/php  
  
# ADD https://phar.phpunit.de/phpunit-5.7.phar /usr/local/bin/phpunit  
COPY phpunit-5.7.phar /usr/local/bin/phpunit  
RUN chmod +x /usr/local/bin/phpunit  
  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set up the command arguments.  
ENTRYPOINT ["/usr/local/bin/phpunit"]  
CMD ["--help"]  
  

