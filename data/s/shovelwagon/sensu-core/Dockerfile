FROM ubuntu:latest  
ENV SENSU_VERSION=0.29.0-7  
RUN \  
apt-get update &&\  
apt-get install -y curl ca-certificates apt-transport-https build-essential
&&\  
curl -s https://sensu.global.ssl.fastly.net/apt/pubkey.gpg | apt-key add - &&\  
. /etc/os-release &&\  
echo "deb https://sensu.global.ssl.fastly.net/apt $UBUNTU_CODENAME main" | tee
/etc/apt/sources.list.d/sensu.list &&\  
apt-get update &&\  
apt-get install -y sensu=${SENSU_VERSION} &&\  
sensu-install -P sensu-plugins-sensu,sensu-plugins-mailer,sensu-plugins-
hipchat,sensu-plugins-slack,sensu-plugins-victorops  
RUN mkdir -p /etc/sensu/conf.d /etc/sensu/check.d /etc/sensu/handlers.d
/etc/sensu/extensions.d /etc/sensu/filters.d /etc/sensu/remediations.d
/etc/sensu/templates  
COPY docker-entrypoint.sh /  
RUN chmod 755 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

