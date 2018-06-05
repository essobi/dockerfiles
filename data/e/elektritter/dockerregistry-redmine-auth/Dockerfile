FROM alpine:latest  
MAINTAINER Rajko Albrecht  
  
RUN apk --no-cache add ruby ruby-irb ruby-json ruby-bigdecimal ruby-rake \  
ruby-io-console ruby-bundler libstdc++ tzdata postgresql-client nodejs \  
libxml2 libxslt libgcrypt sqlite-libs pcre curl postgresql bash procps libffi
\  
&& cp /usr/bin/pg_dump /usr/bin/pg_restore /tmp/ \  
&& apk del --purge postgresql \  
&& mv /tmp/pg_dump /tmp/pg_restore /usr/bin/ \  
&& echo "gem: --no-document" > /etc/gemrc  
  
ENV APP_HOME /srv/docker-redmine-auth  
  
# Copy just the files for bundle install  
ADD vendor/assets $APP_HOME/vendor/assets  
ADD Gemfile $APP_HOME/  
ADD Gemfile.lock $APP_HOME/  
  
ENV BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_IGNORE_MESSAGES=1 \  
BUNDLE_GITHUB__HTTPS=1 \  
NOKOGIRI_USE_SYSTEM_LIBRARIES=1 \  
BUNDLE_FROZEN=1 \  
BUNDLE_PATH=$APP_HOME/vendor/bundle \  
BUNDLE_BIN=$APP_HOME/bin \  
BUNDLE_GEMFILE=$APP_HOME/Gemfile \  
BUNDLE_WITHOUT=development:benchmark:test  
  
RUN apk --no-cache add \--virtual build-dependencies build-base git ruby-dev \  
curl-dev postgresql-dev libxml2-dev libxslt-dev libgcrypt-dev sqlite-dev
libffi-dev libc-dev linux-headers \  
&& bundle install \  
&& apk del --purge build-dependencies  
  
  
ENV RAILS_ENV=production PATH=$APP_HOME/bin:$PATH  
  
# Copy just the files needed for assets:precompile  
ADD Rakefile $APP_HOME/  
ADD config  $APP_HOME/config  
ADD public $APP_HOME/public  
ADD app/assets $APP_HOME/app/assets  
ADD lib/utils $APP_HOME/lib/utils  
ADD app/controllers/application_controller.rb $APP_HOME/app/controllers/  
RUN cd $APP_HOME && rm -rf public/assets && rake assets:precompile
DATABASE_URL=sqlite3:tmp/dummy.db SECRET_KEY_BASE=dummy  
  
ADD . $APP_HOME  
RUN cd $APP_HOME && rake db:migrate  
RUN chown -R nobody:nogroup $APP_HOME  
COPY docker/entrypoint.sh /entrypoint.sh  
COPY docker/production.rb $APP_HOME/config/environments/production.rb  
RUN chmod 755 /entrypoint.sh  
  
USER nobody  
  
WORKDIR $APP_HOME  
ENV HOME $APP_HOME  
  
EXPOSE 3000  
ENTRYPOINT ["/entrypoint.sh"]  
  

