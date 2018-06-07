FROM ruby:2.4.2  
LABEL maintainer="sys0dm1n" \  
description="Guard-sass and Juicer"  
  
RUN gem update --system && gem install guard guard-sass guard-process sass
juicer  
  
RUN gem cleanup cmdparse  
  
#RUN cd /tmp/ && bundle install  
COPY Gemfile /tmp/  
ENV BUNDLE_GEMFILE /tmp/Gemfile  
ENV BUNDLE_JOBS 2  
ENV BUNDLE_PATH /usr/local/bundle  
  
WORKDIR /srv  
  
VOLUME ["/srv"]

