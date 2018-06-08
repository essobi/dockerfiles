FROM ruby:2.2.3  
RUN gem install bundler  
  
ADD ./ /src  
WORKDIR /src  
RUN bundle  
ENTRYPOINT ["/src/bin/sinknode.rb"]  

