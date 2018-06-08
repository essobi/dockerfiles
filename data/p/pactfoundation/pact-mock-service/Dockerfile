FROM ruby:2-alpine  
  
COPY Gemfile /app/  
COPY Gemfile.lock /app/  
RUN apk add --no-cache --virtual build-dependencies build-base && \  
gem install bundler --no-ri --no-rdoc && \  
cd /app; bundle install && \  
gem uninstall bundler && \  
apk del build-dependencies build-base && \  
rm -r ~/.bundle/ /usr/local/bundle/cache  
  
WORKDIR /app  
  
EXPOSE 80  
CMD bundle exec pact-mock-service service --host 0.0.0.0 --port 80 --pact-dir
./pacts  

