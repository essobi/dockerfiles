FROM ruby:2.5.0  
RUN gem install bundler  
  
WORKDIR /app  
ENV HOME /app  
  
COPY ./ /app  
  
RUN bundle  
  
RUN ln -sf /dev/stdout /app/log/heartbeat.log  
ENTRYPOINT /app/bin/heartbeat

