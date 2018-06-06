FROM eher/php  
ENV COMPOSER_HOME /composer  
ENV PATH /composer/vendor/bin:$PATH  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer && rm -rf /tmp/composer-setup.php  
CMD ["-"]  
ENTRYPOINT ["composer", "--ansi"]  

