FROM codeception/codeception  
MAINTAINER Jeckel <jeckel@jeckel.fr>  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y sudo && \  
apt-get clean && rm -rf /var/{lib,cache}/apt && \  
docker-php-ext-install pdo_mysql  
  
COPY codecept.sh /usr/local/bin/codecept.sh  
RUN chmod +x /usr/local/bin/codecept.sh  
  
VOLUME /project  
WORKDIR /project  
  
ENTRYPOINT ["codecept.sh"]

