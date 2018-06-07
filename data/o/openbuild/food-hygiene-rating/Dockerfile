FROM php:7.1-alpine  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
# Make sure we're installing what we think we're installing!  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot \  
&& rm -f /tmp/composer-setup.*  
RUN mkdir /composer-files && cd /composer-files && echo '{"autoload":
{"psr-0": {"Openbuild":"/usr/src/app/"}}}' > composer.json && composer require
guzzlehttp/guzzle && composer require symfony/console  
RUN cd /composer-files && composer dump-autoload -o  
RUN mkdir /downloads && mkdir /export && mkdir /templates  
RUN wget http://ratings.food.gov.uk/open-data-resources/images/images.zip >
/export/images.zip  
COPY ./src/ /usr/src/app  
COPY ./templates/ /templates  
RUN php -r "echo @date('c');" > /export/date.txt  
RUN php /usr/src/app/Openbuild/App.php app:SchemeTypes --autoquit  
RUN php /usr/src/app/Openbuild/App.php app:Ratings --autoquit  
RUN php /usr/src/app/Openbuild/App.php app:Locations --autoquit  
RUN php /usr/src/app/Openbuild/App.php app:Authorities --autoquit  
RUN php /usr/src/app/Openbuild/App.php app:ScoreDescriptors --autoquit  
RUN php /usr/src/app/Openbuild/App.php app:BusinessTypes --autoquit  
RUN php /usr/src/app/Openbuild/App.php app:Establishments --autoquit  
WORKDIR /usr/src/app  
CMD [ "php", "./Openbuild/App.php"]

