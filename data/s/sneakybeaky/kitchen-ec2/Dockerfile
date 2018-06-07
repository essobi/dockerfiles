FROM xueshanf/awscli:latest  
MAINTAINER Jon Barber <jon.barber@acm.org>  
  
ENV RUBY_PACKAGES ruby ruby-dev ruby-rdoc ruby-irb build-base ruby-io-console  
  
# Update and install all of the required packages.  
# At the end, remove the apk cache  
RUN apk update && \  
apk upgrade && \  
apk add $RUBY_PACKAGES && \  
rm -rf /var/cache/apk/*  
  
RUN gem install test-kitchen kitchen-ec2 berkshelf rspec-retry --no-document  

