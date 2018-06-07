FROM ruby:2.5  
WORKDIR /usr/src/app  
  
COPY Gemfile Gemfile.lock ./  
RUN mkdir /logs \  
&& touch /logs/application.log \  
&& ln -sf /dev/stdout /logs/application.log \  
&& cd /usr/src/app \  
&& bundle install  
  
COPY . .  
  
CMD rails db:migrate; rails s

