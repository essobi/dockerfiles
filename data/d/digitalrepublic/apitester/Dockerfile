FROM php:7.1  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
  
RUN apt-get update \  
&& apt-get install -y \  
bash \  
build-essential \  
curl \  
git \  
libicu-dev \  
libgmp3-dev \  
libpcre3-dev \  
openssl \  
sqlite3 \  
unzip \  
wget \  
zlib1g-dev \  
zip \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY docker/install_composer.sh /tmp/install_composer.sh  
  
RUN docker-php-ext-install mbstring zip bcmath json pdo intl gmp \  
&& mkdir /composer \  
&& chmod 777 /composer \  
&& echo "memory_limit=-1" >> "$PHP_INI_DIR/conf.d/99-php-override.ini" \  
&& echo "log_errors=On" >> "$PHP_INI_DIR/conf.d/99-php-override.ini" \  
&& echo "error_log=/dev/stderr" >> "$PHP_INI_DIR/conf.d/99-php-override.ini" \  
&& /tmp/install_composer.sh \  
&& rm /tmp/install_composer.sh \  
&& composer global require hirak/prestissimo \  
&& mkdir /project  
  
WORKDIR /project  
  
COPY ["code/app", "./app"]  
COPY ["code/bin", "./bin"]  
COPY ["code/composer.json", "./"]  
COPY ["code/composer.lock", "./"]  
  
# Build PHP App  
RUN cp app/config/parameters.yml.dist app/config/parameters.yml \  
&& composer install --no-interaction  
  
COPY ./code /project  
  
RUN mkdir -p /var/keys \  
&& openssl genrsa -out /var/keys/private.pem 2048 \  
&& openssl rsa -in /var/keys/private.pem -outform PEM -pubout -out
/var/keys/public.pem  
  
RUN mkdir -p /var/data \  
&& php bin/console doctrine:database:drop --force \  
&& php bin/console doctrine:database:create \  
&& php bin/console doctrine:schema:update --force \  
&& php bin/console sm:fixtures:load \  
&& php bin/console sm:state:set  
  
# Metadata params  
ARG BUILD_DATE  
# ARG VCS_URL  
ARG VCS_REF  
ARG VERSION  
  
# Metadata  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="API Tester" \  
org.label-schema.description="The API Tester is a SmartCloud Platform API
simulator to help during 3rd party application integration." \  
# org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.docker.cmd="docker run -d -p 8080:8080
digitalrepublic/apitester" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vendor="Digital Republic Media Group GmbH" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
EXPOSE 8080  
ADD https://github.com/krallin/tini/releases/download/v0.16.1/tini-static
/bin/tini  
RUN chmod +x /bin/tini  
ENTRYPOINT ["/bin/tini", "-g", "--"]  
CMD ["bin/console", "server:run", "0.0.0.0:8080"]  

