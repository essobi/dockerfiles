FROM ubuntu  
  
RUN apt-get -y update  
RUN apt-get -y install build-essential zlib1g-dev libssl-dev \  
libyaml-dev wget openssl git libreadline-dev libgdbm-dev \  
wget libpq-dev libpq5 libpqxx-4.0 mysql-client \  
libpqxx-dev memcached nodejs nodejs-dev redis-server libxml2 libsasl2-2 \  
libxslt-dev libxml2-dev libgmp-dev libgmp3-dev libgmp10 libmysql++-dev \  
libmysqlclient-dev libmysqld-dev librtmp-dev \  
postgresql-client postgresql-client-common git  
  
RUN cd /tmp && \  
wget http://ftp.ruby-lang.org/pub/ruby/2.2/ruby-2.2.4.tar.gz && \  
tar -xvzf ruby-2.2.4.tar.gz && \  
cd ruby-2.2.4/ && \  
./configure --with-openssl-dir=/usr/bin && \  
make && \  
make install  
  
ADD . /app  
WORKDIR /app  
  
# This should be the host of the BeaconManager Admin Server  
ENV COUPON_URL=${COUPON_URL:-192.168.1.218:3000}  
  
ENV REDISTOGO_URL=${REDISTOGO_URL:-redis://redis:6379}  
ENV BEACONCONTROL_MYSQL_HOST=${BEACONCONTROL_MYSQL_HOST:-mysql}  
ENV BEACONCONTROL_MYSQL_PORT=${BEACONCONTROL_MYSQL_PORT:-3306}  
ENV BEACONCONTROL_MYSQL_USERNAME=${BEACONCONTROL_MYSQL_USERNAME:-root}  
ENV BEACONCONTROL_MYSQL_PASSWORD=${BEACONCONTROL_MYSQL_PASSWORD:-pass}  
ENV SEED_ADMIN_EMAIL=${SEED_ADMIN_EMAIL:-admin@gmail.com}  
ENV SEED_ADMIN_PASSWORD=${SEED_ADMIN_PASSWORD:-test123}  
ENV
KEYCLOAK_ISSUER=${KEYCLOAK_ISSUER:-https://auth.s.orchestracities.com/auth/realms/default}  
ENV KEYCLOAK_PORT=${KEYCLOAK_PORT:-80}  
ENV KEYCLOAK_HOST=${KEYCLOAK_HOST:-auth.s.orchestracities.com}  
ENV KEYCLOAK_CLIENT_ID=${KEYCLOAK_CLIENT_ID:-beacon-manager}  
ENV
KEYCLOAK_CLIENT_SECRET=${KEYCLOAK_CLIENT_SECRET:-bec9ee18-bd3d-4b8f-958a-d797af3eb231}  
ENV
KEYCLOAK_REDIRECT_URI=${KEYCLOAK_REDIRECT_URI:-http://localhost:3000/admins/auth/openid_connect/callback}  
  
ENV
KEYCLOAK_TOKEN_ENDPOINT=${KEYCLOAK_TOKEN_ENDPOINT:-https://auth.s.orchestracities.com/auth/realms/default/protocol/openid-
connect/token}  
ENV
KEYCLOAK_TOKEN_INTROSPECT_ENDPOINT=${KEYCLOAK_TOKEN_INTROSPECT_ENDPOINT:-https://auth.s.orchestracities.com/auth/realms/default/protocol/openid-
connect/token/introspect}  
ENV
KEYCLOAK_USER_INFO_ENDPOINT=${KEYCLOAK_USER_INFO_ENDPOINT:-https://auth.s.orchestracities.com/auth/realms/default/protocol/openid-
connect/userinfo}  
ENV KEYCLOAK_CLIENT_ID=${KEYCLOAK_CLIENT_ID:-beacon-manager}  
  
ENV KEYCLOAK_CLIENT_SECRET=${KEYCLOAK_CLIENT_SECRET}  
ENV KEYCLOAK_REALM_ADMIN_USERNAME=${KEYCLOAK_REALM_ADMIN_USERNAME}  
ENV KEYCLOAK_REALM_ADMIN_PASSWORD=${KEYCLOAK_REALM_ADMIN_PASSWORD}  
ENV KEYCLOAK_REALM_ADMIN_SECRET=${KEYCLOAK_REALM_ADMIN_SECRET}  
  
RUN cd /app && gem install bundler && bundle install  
  
ENTRYPOINT rake db:create && rake db:migrate && rake db:seed && rails s -b
0.0.0.0  

