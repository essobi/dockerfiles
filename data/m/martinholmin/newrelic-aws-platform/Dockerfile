FROM ruby:2.2.3-slim  
MAINTAINER Martin Holmin <martin.holmin@me.com>  
  
ENV APP_HOME /newrelic_aws_cloudwatch_plugin-latest  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
RUN apt-get update -qq && apt-get install -y build-essential libxml2-dev
libxslt1-dev  
  
RUN curl -L https://github.com/newrelic-
platform/newrelic_aws_cloudwatch_plugin/archive/latest.tar.gz > latest.tar.gz  
RUN tar -zxf latest.tar.gz -C /  
ADD ./newrelic_plugin.yml config/newrelic_plugin.yml  
RUN bundle install --jobs 2 --without development test  
RUN rm -rf latest.tar.gz  
RUN apt-get remove -yq --purge build-essential libxml2-dev libxslt1-dev && \  
apt-get autoremove -yq --purge  
  
ENTRYPOINT ["bundle", "exec", "./bin/newrelic_aws"]  

