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
  
RUN mkdir ${composerDir}  
COPY ./composer.json ${composerDir}  
RUN cd ${composerDir} && composer update  
  
# for whalebrew  
LABEL io.whalebrew.name 'phpmd'  
  
WORKDIR /workdir  
  
ENTRYPOINT ["/tools/vendor/bin/phpmd"]  
CMD ["-h"]  

