FROM iron/ruby  
  
MAINTAINER Natalie Akam <natalie.akam@gmail.com>  
  
RUN apk --update add ruby-rdoc ruby-irb  
  
RUN gem install bundler  
  
ADD /unicorn /unicorn  
  
EXPOSE 8080  
WORKDIR /unicorn  
  
RUN bundle install  
  
RUN curl -v http://unicornpoo.herokuapp.com/update/team5-brainiacs/complete  
  
CMD bundle exec rackup --port 8080 --host 0.0.0.0  

