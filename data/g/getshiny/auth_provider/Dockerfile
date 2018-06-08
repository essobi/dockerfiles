FROM ruby:2.4-alpine  
  
# ARG RAILS_ROOT  
# RUN echo "$RAILS_ROOT"  
ENV BUILD_PACKAGES curl-dev ruby-dev build-base  
ENV DEV_PACKAGES tzdata postgresql-dev  
ENV RUBY_PACKAGES ruby-io-console ruby-json yaml nodejs  
  
RUN apk --update --upgrade add $BUILD_PACKAGES $RUBY_PACKAGES $DEV_PACKAGES  
  
ENV RAILS_ROOT /auth_provider  
  
RUN mkdir $RAILS_ROOT  
WORKDIR $RAILS_ROOT  
  
ADD Gemfile $RAILS_ROOT/Gemfile  
ADD Gemfile.lock $RAILS_ROOT/Gemfile.lock  
RUN bundle install  
ADD . $RAILS_ROOT  
  
EXPOSE 3000  
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]  

