FROM ruby:2.3.3  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
RUN mkdir /lacey-admin  
  
ENV RAILS_ENV production  
# ENV RAILS_SERVE_STATIC_FILES true  
# ENV RAILS_LOG_TO_STDOUT true  
WORKDIR /lacey-admin  
COPY Gemfile /lacey-admin/Gemfile  
COPY Gemfile.lock /lacey-admin/Gemfile.lock  
RUN bundle install  
# make port 80 available to the world outside this container  
EXPOSE 80  
COPY . /lacey-admin  
#RUN bundle install  
# CMD puma -C config/puma.rb  

