FROM rebyn/charitymap_ruby  
  
RUN apt-get update -qq  
  
ENV APP_HOME /CharityMap  
# RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD Gemfile* $APP_HOME/  
ADD Gemfile.lock $APP_HOME/  
RUN bundle install  
  
ADD . $APP_HOME  
RUN cp $APP_HOME/config/database.yml.example $APP_HOME/config/database.yml  
CMD ["bundle","exec","rails","server","-b","0.0.0.0","-p","3000"]

