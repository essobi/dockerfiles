FROM tomasce/modulor-base:latest  
MAINTAINER Tomas Celizna <tomas.celizna@gmail.com>  
  
RUN mkdir /app  
WORKDIR /app  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
RUN bundle install --full-index  
ADD . /app  
RUN rm -rf /app/.bundle  
  
EXPOSE 3000  
CMD ["puma", "config.ru", "-C", "config/puma.rb"]  

