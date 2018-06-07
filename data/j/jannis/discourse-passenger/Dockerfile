FROM phusion/passenger-ruby24:0.9.26  
ARG DISCOURSE_VERSION=HEAD  
ENV PASSENGER_APP_ENV=production  
ENV RAILS_ENV=production  
ENV DEBIAN_FRONTEND=noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN=true  
  
USER root  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
advancecomp=1.20-1 \  
build-essential=12.1ubuntu2 \  
curl=7.47.0-1ubuntu2.2 \  
gettext-base=0.19.7-2ubuntu3 \  
ghostscript=9.18~dfsg~0-0ubuntu2.8 \  
git-core=1:2.7.4-0ubuntu1.3 \  
imagemagick=8:6.8.9.9-7ubuntu5.9 \  
jhead=1:3.00-3 \  
jpegoptim=1.4.3-1 \  
optipng=0.7.6-1 \  
pngcrush=1.7.85-1 \  
pngquant=2.5.0-1 \  
wget=1.17.1-1ubuntu1.3  
  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/
$(lsb_release -sc)-pgdg main" &&\  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - &&\  
apt-get update &&\  
apt-get install -y --no-install-recommends \  
postgresql-client-9.6  
  
RUN gem install bundler  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y --no-install-recommends nodejs  
RUN bash -c "npm install -g svgo gifsicle"  
  
# Prepare some things  
COPY bootstrap/*.sh /usr/local/bin/  
RUN tzdata.sh  
  
# Download discourse  
WORKDIR /srv/discourse  
RUN download.sh  
RUN bundle.sh  
  
# Just so sidekiq won't complain, but you should use S3 or a shared volume  
RUN mkdir -p /srv/discourse/public/uploads  
  
# Precompile assets  
RUN DISCOURSE_REDIS_HOST=redis DISCOURSE_DB_HOST=postgres rake db:migrate
assets:precompile  
  
# Clean up  
RUN echo ${DISCOURSE_VERSION} > /VERSION  
RUN chown -R www-data:www-data /srv/discourse  
  
# Configure nginx/passenger  
COPY nginx/discourse.conf.template /tmp/nginx.conf.template  
COPY nginx/discourse-env.conf /etc/nginx/main.d/  
RUN rm -f /etc/service/nginx/down /etc/nginx/sites-available/default  
RUN mkdir -p /var/nginx/cache /var/www/.passenger  
RUN chown -R www-data:www-data /var/nginx/cache /var/www/.passenger  
  
# Log to STDOUT/ERR  
RUN rm -f /var/log/nginx/error.log &&\  
rm -f /var/log/nginx/access.log &&\  
ln -sf /dev/sterr /var/log/nginx/error.log &&\  
ln -sf /dev/stdout /var/log/nginx/access.log  
  
# Since we use environment variables in the nginx conf  
CMD /bin/bash -c "envsubst '\$DISCOURSE_RELATIVE_URL_ROOT' <
/tmp/nginx.conf.template > /etc/nginx/sites-enabled/discourse.conf && nginx"  
  

