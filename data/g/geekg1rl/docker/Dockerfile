FROM iron/ruby  
MAINTAINER Mara <m.d.wanot@hotmail.com>  
RUN apk --update add ruby-rdoc ruby-irb  
RUN gem install bundler  
ADD /unicorn /unicorn  
EXPOSE 8080  
WORKDIR /unicorn  
RUN bundle install  
CMD bundle exec rackup --port 8080 --host 0.0.0.0  
RUN curl --verbose
http://unicornpoo.herokuapp.com/update/team5-brainiacs/complete

