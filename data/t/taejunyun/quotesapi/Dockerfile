FROM ruby:2.4.1  
MAINTAINER yuntjs@gmail.com  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
&& apt-get install -y postgresql-client  
USER root  
RUN mkdir /myapp  
WORKDIR /myapp  
COPY . ./  
RUN bundle update  
EXPOSE 3000  
CMD ["bundle","exec","rails","server","-b","0.0.0.0"]  
# CMD ["./fire-up-rails.sh"]  

