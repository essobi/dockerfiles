FROM ruby:2.3.1  
ENV BUILD_PACKAGES="build-essential" \  
DEV_PACKAGES="libxml2-dev libxslt-dev libsqlite3-dev postgresql-server-dev-all
libmysqlclient-dev tzdata nodejs" \  
SYSTEM_LIB_REQUIRED_GEMS="mysql2 pg" \  
GEMS="sqlite3 debug_inspector binding_of_caller byebug puma rails bcrypt
byebug therubyracer rake minitest i18n addressable ast execjs connection_pool
orm_adapter ipaddress request_store rspec rspec-support tilt spring timecop
turbolinks-source faker warden rack-protection launchy parser autoprefixer-
rails uglifier coffee-script better_errors rdoc pry rspec-core rspec-
expectations rspec-mocks slim spring-commands-rspec turbolinks letter_opener
astrolabe faraday faraday_middleware sdoc factory_girl bullet jbuilder onkcop
annotate bitmask_attributes polyamorous gon ransack simple_form coffee-rails
responders devise gretel xray-rails" \  
RUBY_VERSION="2.3.1"  
# preinstall native extensions  
RUN set -x \  
&& apt-get update -y \  
&& apt-get install -y $BUILD_PACKAGES $DEV_PACKAGES \  
&& gem install nokogiri -- \  
\--with-xml2-config=/usr/bin/xml2-config \  
\--with-xslt-config=/usr/bin/xslt-config \  
&& gem install $SYSTEM_LIB_REQUIRED_GEMS \-- --use-system-libraries \  
&& gem install $GEMS \  
&& rm -rf /usr/local/bundle/cache/*.gem \  
&& rm -rf /usr/local/lib/ruby/gems/$RUBY_VERSION/cache/*.gem \  
&& rm -rf ~/.gem \  
&& rm -rf /usr/lib/libmysqld* /usr/bin/mysql*  
  
# support Japanese input in Rails Console  
ENV LANG C.UTF-8  
# rails default port  
EXPOSE 3000  
WORKDIR /app  
  
ONBUILD ADD scripts/ /app/  
ONBUILD COPY local_gems /app/local_gems  
ONBUILD RUN ls local_gems  
ONBUILD COPY Gemfile /app/  
ONBUILD COPY Gemfile.lock /app/  
ONBUILD RUN $(test -x pre_config.sh && sh pre_config.sh) || true  
ONBUILD RUN bundle install -j16  
ONBUILD RUN $(test -x post_config.sh && sh post_config.sh) || true  

