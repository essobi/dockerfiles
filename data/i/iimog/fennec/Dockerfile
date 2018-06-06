FROM php:7.1-apache  
ARG BRANCH=master  
LABEL maintainer="markus.ankenbrand@uni-wuerzburg.de"  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update \  
&& apt-get install -yq nodejs git postgresql-client libpq-dev unzip vim
libdbd-pg-perl liblog-log4perl-perl yarn jq cron\  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install pdo pdo_pgsql zip \  
&& a2enmod rewrite \  
&& docker-php-source delete  
RUN pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug  
RUN git clone \--branch ${BRANCH} \--recursive
https://github.com/molbiodiv/fennec /fennec  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
COPY php.ini /usr/local/etc/php/  
COPY parameters.yml /fennec/app/config/  
RUN cd /fennec; composer install --no-interaction  
  
RUN npm install -g coffeescript@1.12.7  
RUN cd /fennec; yarn install --non-interactive  
RUN cd /fennec; ./node_modules/.bin/encore production  
# RUN cd /fennec; ./node_modules/.bin/encore dev  
RUN cd /fennec/web/assets/Phinch; coffee -o scripts src  
  
RUN rm -rf /var/www/html && ln -fs /fennec/web /var/www/html  
RUN chown -R www-data:www-data /fennec/var  
  
RUN echo "export LC_ALL=C.UTF-8" >>/etc/apache2/envvars  
RUN echo "export LANG=C.UTF-8" >>/etc/apache2/envvars  
  
# Install conda  
RUN curl -sS https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh >miniconda.sh  
RUN chmod +x miniconda.sh  
RUN ./miniconda.sh -b -f -p /usr/local  
RUN conda install --yes -c bioconda biom-format=2.1.6  
# Install sphinx to build documentation  
RUN conda install --yes sphinx  
  

