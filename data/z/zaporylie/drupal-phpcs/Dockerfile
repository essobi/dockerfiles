FROM drupaldocker/php:fpm  
  
MAINTAINER Jakub Piasecki <jakub@piaseccy.pl>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get -yq install shunit2 curl git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require drupal/coder  
  
RUN mkdir /root/.ssh  
RUN echo "Host *\n\tStrictHostKeyChecking no\n\tUserKnownHostsFile
/dev/null\n" >> /root/.ssh/config  
  
VOLUME /reports  
VOLUME /workspace  
  
ENV SHA=HEAD \  
SHA_BEFORE=HEAD~1 \  
CLONE_PATH=/workspace \  
SERVICE="github.com" \  
USERNAME=drupal \  
REPOSITORY=drupal \  
METHOD=http \  
BRANCH=7.x \  
DEPTH=20 \  
REPORT_FORMAT="checkstyle" \  
REPORT_PATH="/reports" \  
REPORT_FILENAME="checkstyle-result.xml" \  
EXTENSIONS="php|module|inc|install|test|profile|theme|js|css|info|txt" \  
INCLUDE="." \  
DEBUG=FALSE  
  
COPY test.sh /tmp/test.sh  
  
RUN chmod +x /tmp/test.sh  
  
CMD ["/tmp/test.sh"]  

