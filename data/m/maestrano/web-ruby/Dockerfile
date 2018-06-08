FROM ruby:2.3  
# Install System libraries  
RUN apt-get update && apt-get install -y \  
git \  
imagemagick \  
nginx \  
supervisor \  
awscli \  
&& rm -rf /var/lib/apt/lists/*  
  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \  
gpg --keyserver hkp://keyserver.pgp.com:80 --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.12.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Install foreman and popular gems  
RUN gem install foreman \  
coffee-rails:4.0.1 \  
bcrypt-ruby:3.1.2 \  
bootstrap-sass:2.3.2.0 \  
bootstrap-will_paginate:0.0.9 \  
execjs:2.7.0 \  
intercom:3.5.4 \  
jbuilder:1.0.2 \  
jbuilder:2.2.16 \  
jquery-rails:3.0.4 \  
jquery-rails:4.1.1 \  
mno-enterprise:3.1.0 \  
mno-enterprise:3.1.2 \  
newrelic_rpm:3.16.2.321 \  
omniauth-facebook:2.0.1 \  
omniauth-google-oauth2:0.2.10 \  
omniauth-linkedin-oauth2:0.1.5 \  
omniauth-openid:1.0.1 \  
pg:0.18.4 \  
pg:0.15.1 \  
puma:3.4.0 \  
puma:3.6.0 \  
rails:5.0 \  
rails:4.2.10 \  
rails_12factor:0.0.3 \  
rails_12factor:0.0.2 \  
rake:11.2.2 \  
sass-rails:4.0.1 \  
sass-rails:5.0.6 \  
sparkpost:0.1.4 \  
sprockets:2.11.0 \  
sqlite3:1.3.11 \  
therubyracer:0.12.2 \  
turbolinks:1.1.1 \  
uglifier:2.1.1 \  
uglifier:3.0.2 \  
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
HEALTHCHECK \--timeout=5s CMD bash /usr/local/bin/healthcheck.sh  
  
# Entrypoint command  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf" ]  

