FROM ruby:latest  
MAINTAINER maxime.visonneau@gmail.com  
  
# CONFD  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 /usr/local/bin/confd  
ADD confd /etc/confd  
  
ADD pptcb /usr/bin/pptcb  
  
RUN \  
apt-get update && \  
apt-get install -y cron && \  
apt-get clean && apt-get autoclean && \  
gem install zip && \  
chmod +x /usr/local/bin/confd && \  
touch /var/log/cron.log  
  
VOLUME [ "/etc/puppetlabs/code/environments" ]  
  
# RUNTIME  
ADD docker-entrypoint /docker-entrypoint  
ADD docker-entrypoint.d /docker-entrypoint.d  
ENTRYPOINT ["/docker-entrypoint"]  

