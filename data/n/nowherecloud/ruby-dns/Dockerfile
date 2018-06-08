FROM ruby:2.4  
  
COPY bootstrapper-dnsd.sh /srv  
  
COPY Gemfile /srv  
  
COPY dnsd.rb /srv  
  
RUN chmod a+x /srv/bootstrapper-dnsd.sh \  
&& BUNDLE_GEMFILE=/srv/Gemfile bundler install --without rest_api amqp_api  
  
EXPOSE 53/udp 53/tcp  
  
ENV DNS_TTL=10 \  
DNS_PORT=53 \  
DNS_SUFFIX=nowhere.dev \  
MYSQL_USER=change-me \  
MYSQL_PASS=change-me \  
MYSQL_DB=change-me \  
USE_DOCKER_BIND=false \  
UPSTREAM_DNS1_IP=208.67.222.222 \  
UPSTREAM_DNS1_PORT=53 \  
UPSTREAM_DNS2_IP=208.67.220.220 \  
UPSTREAM_DNS2_PORT=53  
  
ENTRYPOINT ["/srv/bootstrapper-dnsd.sh"]  

