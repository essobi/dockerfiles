FROM ruby:stretch  
  
ENV APP_HOME /mikeyockey-rails  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
COPY Gemfile* $APP_HOME/  
RUN bundle install  
  
COPY . $APP_HOME  
EXPOSE 3000  
ENTRYPOINT ["bin/rails"]  

