FROM emergya/ubuntu_16.04-apache-php-mysql:201705191145-8d1948b  
  
ENV BUILD_TIMESTAMP 201704171337  
ENV WP_VERSION latest  
ARG WP_VERSION=latest  
ENV WP_CLI_VERSION 1.1.0  
ARG WP_CLI_VERSION=1.1.0  
RUN curl -sL "https://github.com/wp-cli/wp-
cli/releases/download/v$WP_CLI_VERSION/wp-cli-$WP_CLI_VERSION.phar" -o
/usr/bin/wp && \  
chmod +x /usr/bin/wp  
  
ADD assets /assets  
  
ENTRYPOINT ["/assets/bin/entrypoint-wordpress"]  

