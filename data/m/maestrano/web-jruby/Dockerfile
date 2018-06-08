FROM jruby:9.1.10  
# Install System libraries  
RUN apt-get update && apt-get install -y \  
git \  
imagemagick \  
nginx \  
supervisor \  
awscli \  
&& rm -rf /var/lib/apt/lists/*  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 7.2.1  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
  
# Install foreman and popular gems  
RUN gem install \  
activeadmin:1.0.0.pre4 \  
activemerchant:1.55.0 \  
activerecord-jdbc-adapter \  
activerecord-jdbcmysql-adapter:1.3.19 \  
activerecord-session_store:0.1.2 \  
attr_encrypted:1.4.0 \  
coffee-rails:4.0.1 \  
bcrypt-ruby:3.1.2 \  
bootstrap-sass:2.3.2.0 \  
bootstrap-will_paginate:0.0.9 \  
braintree:2.58.0 \  
cancan:1.6.10 \  
carrierwave:0.10.0 \  
coffee-rails:4.1.1 \  
config:1.1.1 \  
config:1.2.1 \  
connection_pool:2.2.0 \  
countries:1.2.5 \  
deep_merge:1.0.1 \  
devise:3.5.6 \  
devise-async:0.10.1 \  
encryptor:1.3.0 \  
eventbrite-api:0.0.3 \  
execjs:2.7.0 \  
figaro:1.1.1 \  
fog:1.37.0 \  
foreman \  
geocoder:1.3.1 \  
haml-rails:0.9.0 \  
httparty:0.13.7 \  
httparty:0.14.0 \  
jbuilder:1.0.2 \  
jbuilder:2.2.16 \  
jbuilder:2.4.1 \  
jdbc-mysql \  
jdbc-mysql:5.1.38 \  
jdbc-postgres \  
jdbc-sqlite3 \  
jquery-rails:3.0.4 \  
jquery-rails:4.1.0 \  
jquery-rails:4.1.1 \  
json_api_client:1.3.0 \  
json_builder:3.1.7 \  
kramdown:1.11.1 \  
kramdown:1.12.0 \  
maxminddb:0.1.11 \  
mini_magick:4.1.0 \  
minitest:5.9.1 \  
myob-essentials-api:0.0.2 \  
mongoid:5.1.6 \  
mongoid-tree \  
mongoid-history \  
money:6.7.0 \  
money:6.7.1 \  
money-rails:1.6.0 \  
money-rails:1.7.0 \  
newrelic_rpm:3.17.2.327 \  
nex_client:0.14.0 \  
nokogiri:1.6.8.1 \  
oauth2:1.1.0 \  
puma:3.6.0 \  
puma:3.7.0 \  
pusher:1.3.0 \  
rails:5.0 \  
rails:4.2.8 \  
rails_12factor:0.0.3 \  
rails_12factor:0.0.2 \  
rake:10.5.0 \  
rake:11.2.2 \  
rake:11.3.0 \  
redis:3.2.2 \  
redis-rails:4.0.0 \  
redis-rails:5.0.1 \  
redis-store:1.1.7 \  
retriable:2.1.0 \  
ruby-openid:2.7.0 \  
ruby-saml-idp:0.3.2 \  
sass:3.4.21 \  
sass-rails:4.0.1 \  
sass-rails:5.0.6 \  
sidekiq:4.1.0 \  
sidekiq:4.2.10 \  
sidekiq-cron:0.4.3 \  
sinatra:1.4.7 \  
sparkpost:0.1.4 \  
sprockets:2.11.0 \  
sprockets-helpers:1.2.1 \  
therubyrhino \  
timezone:0.6.0 \  
turbolinks:1.1.1 \  
uglifier:2.1.1 \  
uglifier:3.0.2 \  
warden:1.2.6 \  
will_paginate:3.0.4 \  
\--no-ri --no-rdoc --verbose  
  
# App Support tools  
RUN mkdir -p /app_support/geocoder \  
&& touch /app_support/geocoder/geodb.mmdb \  
&& curl -s
"http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz" |
gunzip -c > /app_support/geocoder/geodb.mmdb \  
&& chown -R www-data:www-data /app_support  
  
# Setup  
RUN mkdir -p /app /var/log/app \  
&& rm -f /etc/nginx/sites-enabled/* \  
&& chown -R www-data:www-data /app /var/log/app  
  
# Configuration  
COPY nginx.conf /etc/nginx/  
COPY app.conf /etc/nginx/sites-enabled/  
COPY supervisord.conf /etc/supervisor/  
# Expose 80  
EXPOSE 80  
# Healthcheck  
COPY healthcheck.sh /usr/local/bin/  
HEALTHCHECK --timeout=5s CMD bash /usr/local/bin/healthcheck.sh  
  
# Entrypoint command  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf" ]  

