FROM iron/ruby  
MAINTAINER mispelaur and d903xp your@email.com  
RUN apk --update add ruby-rdoc ruby-irb  
RUN gem install bundler  
RUN curl http://unicornpoo.herokuapp.com/update/team3-scuzzbuckets/complete  
ADD /unicorn /unicorn  
EXPOSE 8080  
WORKDIR /unicorn  
RUN bundle install  
CMD bundle exec rackup --port 8080 --host 0.0.0.0

