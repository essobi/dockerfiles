FROM ruby:2.4-alpine  
  
ENV RAILS_ENV=production  
  
RUN apk --no-cache add --upgrade \  
build-base \  
libxml2-dev \  
libxslt-dev \  
postgresql-dev \  
tzdata \  
&& rm -rf /var/cache/apk/*  
  
ADD ./ ./  
  
RUN bundle install --without development test  
  
CMD bundle exec rake db:migrate && bundle exec rails server -e production  
  

