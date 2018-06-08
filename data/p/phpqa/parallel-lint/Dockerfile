# Set defaults  
ARG COMPOSER_IMAGE="composer:1.6.4"  
ARG BASE_IMAGE="php:7.2-alpine"  
ARG PACKAGIST_NAME="jakub-onderka/php-parallel-lint"  
ARG PHPQA_NAME="php-parallel-lint"  
ARG VERSION="1.0.0"  
# Download with Composer - https://getcomposer.org/  
FROM ${COMPOSER_IMAGE} as composer  
ARG PACKAGIST_NAME  
ARG VERSION  
RUN COMPOSER_HOME="/composer" \  
composer global require --prefer-dist --no-progress --dev
${PACKAGIST_NAME}:${VERSION}  
  
# Build image  
FROM ${BASE_IMAGE}  
ARG PHPQA_NAME  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
ARG IMAGE_NAME  
  
# Install Tini - https://github.com/krallin/tini  
RUN apk add --no-cache tini  
  
# Install PHP Parallel Lint - https://github.com/JakubOnderka/PHP-Parallel-
Lint  
COPY \--from=composer "/composer/vendor" "/vendor/"  
ENV PATH /vendor/bin:${PATH}  
  
# Add entrypoint script  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
# Add image labels  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.vendor="phpqa" \  
org.label-schema.name="${PHPQA_NAME}" \  
org.label-schema.version="${VERSION}" \  
org.label-schema.build-date="${BUILD_DATE}" \  
org.label-schema.url="https://github.com/phpqa/${PHPQA_NAME}" \  
org.label-schema.usage="https://github.com/phpqa/${PHPQA_NAME}/README.md" \  
org.label-schema.vcs-url="https://github.com/phpqa/${PHPQA_NAME}.git" \  
org.label-schema.vcs-ref="${VCS_REF}" \  
org.label-schema.docker.cmd="docker run --rm --volume \${PWD}:/app --workdir
/app ${IMAGE_NAME}"  
  
# Package container  
WORKDIR "/app"  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["parallel-lint"]  

