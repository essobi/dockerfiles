FROM ruby:2.4.3  
ENV INSTALL_PATH /app_folder  
  
RUN mkdir -p $INSTALL_PATH  
WORKDIR $INSTALL_PATH  
  
RUN apt-get update && apt-get install -qq -y build-essential nodejs libpq-dev  
  
COPY Gemfile* $INSTALL_PATH/  
  
RUN bundle install \  
\--without development test \  
\--jobs=4 \  
\--deployment  
  
COPY . $INSTALL_PATH/  
  
ENV RAILS_ENV production  
ENV LOG_LEVEL info  
  
RUN bundle exec rake assets:precompile  
  
EXPOSE 3000  
CMD ["bundle", "exec", "rails", "server", "--binding=0.0.0.0" ]  

