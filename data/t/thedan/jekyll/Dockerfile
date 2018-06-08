FROM ruby:2.1.10  
ADD . /jekyll  
WORKDIR /jekyll  
RUN script/bootstrap  
RUN bundle exec rake build  
RUN ls pkg/*.gem | head -n 1 | xargs gem install -l  
WORKDIR /source  
ENTRYPOINT ["jekyll", "build", "-f", "-t", "-V"]  

