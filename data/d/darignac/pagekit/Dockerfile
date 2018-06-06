FROM php:7-fpm  
MAINTAINER Alexander Herrmann <darignac@gmail.com>  
ENV PAGEKIT_VERSION=1.0.10  
ENV PAGEKIT_USERNAME=admin  
ENV PAGEKIT_PASSWORD=password  
ENV PAGEKIT_TITLE=Pagekit  
ENV PAGEKIT_MAIL=admin@example.com  
ENV PAGEKIT_DB_DRIVER=mysql  
ENV PAGEKIT_DB_PREFIX=pk_  
ENV PAGEKIT_DB_HOST=  
ENV PAGEKIT_DB_NAME=  
ENV PAGEKIT_DB_USERNAME=  
ENV PAGEKIT_DB_PASSWORD=  
ENV PAGEKIT_LOCALE=en_GB  
RUN apt-get update \  
&& apt-get -y install \  
unzip \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install zip pdo_mysql \  
&& docker-php-source delete \  
&& mkdir -p /pagekit \  
&& mkdir -p /pagekit-custom \  
&& mkdir -p /pagekit-config  
WORKDIR /pagekit  
RUN wget
https://github.com/pagekit/pagekit/releases/download/${PAGEKIT_VERSION}/pagekit-${PAGEKIT_VERSION}.zip
-O /pagekit/pagekit.zip \  
&& unzip /pagekit/pagekit.zip \  
&& rm /pagekit/pagekit.zip \  
&& chown www-data:www-data -R /pagekit \  
&& chmod g+w -R /pagekit \  
&& chmod +x /pagekit/pagekit  
ADD entrypoint.sh /pagekit  
RUN chmod +x /pagekit/entrypoint.sh  
VOLUME ["/pagekit", "/pagekit-custom"]  

