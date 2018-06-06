FROM ubuntu:16.04  
MAINTAINER Brice Argenson <brice@clevertoday.com>  
  
ENV SENSU_CONFIG /etc/sensu  
  
RUN apt-get -y update && apt-get install -y apt-transport-https rsync wget vim
iputils-ping && \  
wget -q https://sensu.global.ssl.fastly.net/apt/pubkey.gpg -O- | apt-key add -
&& \  
echo "deb https://sensu.global.ssl.fastly.net/apt sensu main" >
/etc/apt/sources.list.d/sensu.list && \  
apt-get -y update && apt-get install -y sensu  
  
RUN apt-get -y update && apt-get install -y ruby ruby-dev build-essential
zlib1g-dev && \  
gem install mail json sensu-plugin net-ping inifile sys-proctable em-http-
request nokogiri nori rest-client --no-ri --no-rdoc  
  
VOLUME /conf.d  
VOLUME /plugins  
VOLUME /handlers  
  
COPY config $SENSU_CONFIG/conf.d  
COPY plugins $SENSU_CONFIG/plugins  
COPY extensions $SENSU_CONFIG/extensions  
COPY handlers $SENSU_CONFIG/handlers  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

