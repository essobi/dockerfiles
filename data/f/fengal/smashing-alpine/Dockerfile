  
FROM ruby:alpine  
  
RUN apk add --update g++ make nodejs  
RUN gem install bundler smashing tzinfo-data  
RUN mkdir /smashing && \  
smashing new smashing && \  
cd /smashing  
RUN printf "gem 'tzinfo-data'\n" >> Gemfile  
RUN printf "gem 'thin'" >> Gemfile  
RUN bundle  
  
VOLUME ["/smashing"]  
  
ENV PORT 3030  
EXPOSE $PORT  
WORKDIR /smashing  
  
CMD /usr/local/bundle/bin/bundle install; /usr/local/bundle/bin/smashing start  

