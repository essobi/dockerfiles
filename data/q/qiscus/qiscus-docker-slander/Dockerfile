FROM ruby:2.1.1  
MAINTAINER Fitra Aditya "fitra@g.pl"  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# create app folder  
ENV APP_HOME /qiscus_slander  
RUN mkdir $APP_HOME  
  
# copy the app into the image  
ADD . $APP_HOME  
  
# now that the app is here, we can bundle  
WORKDIR $APP_HOME  
RUN bundle install  
  
CMD ["/bin/bash", "-c", "ruby /qiscus_slander/slander.rb"]

