FROM ruby:2.4.1  
RUN mkdir /make-it-rain  
  
COPY Gemfile* /tmp/  
WORKDIR /tmp  
  
RUN bundle install --jobs 10  
  
WORKDIR /make-it-rain  
ADD . /make-it-rain  
  
ENTRYPOINT puma -p 3000  

