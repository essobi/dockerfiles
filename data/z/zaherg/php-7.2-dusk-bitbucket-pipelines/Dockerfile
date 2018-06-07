FROM php:7.2  
  
ARG BUILD_DATE  
ARG VCS_REF  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
LABEL Maintainer="Zaher Ghaibeh <z@zah.me>" \  
Description="A simple PHP 7.2 image which contain just the minimum required to
run Dusk on bitbucket pipelines." \  
org.label-schema.name="php-7.2-dusk-bitbucket-pipelines" \  
org.label-schema.description="A simple PHP 7.2 image which contain just the
minimum required to run Dusk on bitbucket pipelines." \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/linuxjuggler/php-7.2-dusk-
bitbucket-pipelines" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0"  
  
  
RUN apt-get update \  
&& apt-get install -y unzip zlib1g-dev libxpm4 libxrender1 libgtk2.0-0 libnss3
libgconf-2-4 \  
chromium xvfb gtk2-engines-pixbuf xfonts-cyrillic xfonts-100dpi xfonts-75dpi
xfonts-base xfonts-scalable \  
imagemagick x11-apps \  
&& docker-php-ext-install zip \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN Xvfb -ac :0 -screen 0 1280x1024x16 &  

