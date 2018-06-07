FROM inventis/php:7.2  
LABEL maintainer="Jan Esser <jane@inventis.be>"  
  
# install composer  
RUN curl https://getcomposer.org/composer.phar -o /usr/local/bin/composer &&
chmod +x /usr/local/bin/composer  
  
RUN apt-get update && apt-get install -y ssh openssh-client git  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
RUN mkdir -p ~/.ssh/  
RUN touch ~/.ssh/known_hosts  
COPY known-host-domains /known-host-domains  
RUN while read in; do ssh-keyscan -H "$in" >> ~/.ssh/known_hosts; done <
/known-host-domains  
  
ADD https://github.com/krallin/tini/releases/download/v0.17.0/tini-static
/sbin/tini  
RUN chmod +x /sbin/tini  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["composer"]

