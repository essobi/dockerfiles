FROM debian:squeeze  
# Install modules  
RUN apt-get update && apt-get install -y \  
php5 php5-intl php5-mcrypt php5-xsl \  
php5-curl php5-gd php5-xdebug \  
curl git  
WORKDIR /app  
RUN mkdir /root/.ssh -m 0700  
RUN mkdir /root/.composer  
COPY deploybot_key /root/.ssh/id_rsa  
RUN chmod 0600 /root/.ssh/id_rsa  
COPY known_hosts /root/.ssh/known_hosts  
RUN chmod 0644 /root/.ssh/known_hosts  
COPY composer.config /root/.composer/config.json

