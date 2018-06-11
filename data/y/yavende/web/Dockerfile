FROM ruby:2.3.1  
RUN apt-get update -qq  
RUN apt-get install -y \  
nodejs \  
jpegoptim \  
optipng  
  
ARG APP_ROOT=/source  
RUN mkdir $APP_ROOT  
WORKDIR $APP_ROOT  
  
COPY Gemfile* $APP_ROOT/  
RUN bundle install --retry=3  
  
COPY . $APP_ROOT  
  
# So other prograqms like postgres can add stuff here  
RUN chmod -R 0777 $APP_ROOT/public  
  
CMD "./scripts/run_server.sh"  

