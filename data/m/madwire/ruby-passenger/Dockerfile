FROM ruby:2.3  
MAINTAINER Richard Adams richard@madwire.co.uk  
  
ENV PORT=80  
ENV MIN_INSTANCES=1  
ENV MAX_POOL_SIZE=3  
RUN gem install passenger && passenger-config install-standalone-runtime  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY Gemfile /usr/src/app/  
ONBUILD COPY Gemfile.lock /usr/src/app/  
ONBUILD RUN bundle config --global frozen 1 && bundle install --jobs 4
--deployment --without development test  
  
ONBUILD COPY . /usr/src/app  
ONBUILD RUN RAILS_ENV=production SECRET_KEY_BASE=temp bundle exec rake
assets:precompile  
  
CMD sh -c 'passenger start -p $PORT --max-pool-size $MAX_POOL_SIZE --min-
instances $MIN_INSTANCES --log-file /dev/stdout'  

