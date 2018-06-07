FROM 4armed/heartbleed-ruby  
MAINTAINER Marc Wickenden <marc@4armed.com>  
  
RUN apt-get update && apt-get install -y build-essential  
  
RUN echo 'gem: --no-rdoc --no-ri' >> $HOME/.gemrc && \  
gem install bundler  
  
RUN gem install foreman  
  
# Downgrade ssl for Heartbleed  
RUN apt-get update && apt-get -y --force-yes install libcurl4-openssl-dev
libssl-dev=1.0.1-4ubuntu3 libssl1.0.0=1.0.1-4ubuntu3 openssl=1.0.1-4ubuntu3
libmysqlclient-dev libpq-dev imagemagick libmagickwand-dev && rm -rf
/var/lib/apt/lists/*  
  
ENV RAILS_ENV production  
ENV RACK_ENV production  
  
WORKDIR /app  
ONBUILD ADD . /app  
ONBUILD RUN bundle install --without development test  
ONBUILD RUN bundle exec rake assets:precompile  

