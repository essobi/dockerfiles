FROM ruby:2.4.1  
MAINTAINER "Martin Kapp <martin@coderats.net>"  
LABEL name="Base Ruby 2.4 image with NodeJS 6 and bundler"  
LABEL version="1.1"  
  
# Install Node v6. Required for something.  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN gem install bundler -v 1.15.3 --no-rdoc --no-ri  

