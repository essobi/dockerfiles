FROM ruby:2.1.5  
MAINTAINER Dmitry Mozzherin  
ENV LAST_FULL_REBUILD 2015-06-24  
RUN apt-get install libmysqlclient-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN bundle config --global frozen 1  
RUN mkdir -p /app  
WORKDIR /app  
COPY Gemfile /app/  
COPY Gemfile.lock /app/  
RUN bundle install --without development test  
COPY . /app  
RUN cp /app/config/env.sh.example /app/config/env.sh  
  
CMD ["unicorn", "-c", "/app/config/docker/unicorn.rb"]  
  

