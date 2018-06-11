FROM iron/ruby  
  
MAINTAINER Lucy and Maloney <lucyfang2@gmail.com>  
  
RUN apk --update add ruby-rdoc ruby-irb  
  
RUN gem install bundler  
  
ADD /unicorn /unicorn  
  
EXPOSE 8080  
WORKDIR /unicorn  
  
RUN bundle install  
  
RUN curl --verbose
http://unicornpoo.herokuapp.com/update/team3-scuzzbuckets/complete  

