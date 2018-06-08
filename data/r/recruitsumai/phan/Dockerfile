FROM php:7  
ARG composerDir="/tools"  
RUN apt-get update && apt-get install -y \  
git \  
unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN git clone https://github.com/nikic/php-ast.git \  
&& cd php-ast \  
&& phpize \  
&& ./configure \  
&& make install \  
&& echo 'extension=ast.so' > /usr/local/etc/php/php.ini \  
&& cd .. && rm -rf php-ast  
  
RUN mkdir ${composerDir}  
COPY ./composer.json ${composerDir}  
RUN cd ${composerDir} && composer update  
  
# for whalebrew  
LABEL io.whalebrew.name 'phan'  
  
WORKDIR /workdir  
  
ENTRYPOINT ["/tools/vendor/bin/phan"]  
CMD ["-h"]  

