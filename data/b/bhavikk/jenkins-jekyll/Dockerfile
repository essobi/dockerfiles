FROM jenkins:alpine  
MAINTAINER Bhavik Kumar <contact@bhavik.io>  
  
# Switch to root  
USER root  
  
# Update everything  
RUN apk update && apk upgrade  
  
# Install pre-reqs for Jekyll  
RUN apk --update --no-cache add build-base ruby ruby-dev ruby-rdoc ruby-irb
ruby-json ruby-rake ruby-io-console libffi-dev  
  
# Install Jekyll  
RUN gem update --system --no-document  
RUN gem install jekyll --no-document  
RUN gem install jekyll-paginate --no-document  
RUN gem clean && gem sources --clear-all  
  
# Clean up  
RUN apk del build-base libffi-dev ruby-dev  
RUN rm -rf /usr/lib/ruby/gems/*/cache/*.gem  
  
# Switch back to jenkins  
USER jenkins  

