FROM heroku/cedar:14  
MAINTAINER Glenn Gillen <me@glenngillen.com>  
  
RUN mkdir -p /app/user  
  
ENV GEM_PATH /app/heroku/ruby/bundle/ruby/2.1.7  
ENV GEM_HOME /app/heroku/ruby/bundle/ruby/2.1.7  
ENV BUNDLE_PATH=/bundle  
RUN mkdir -p /app/heroku/ruby/bundle/ruby/2.1.7  
  
# Install Ruby  
RUN mkdir -p /app/heroku/ruby/ruby-2.1.7 && curl -s --retry 3 -L
https://heroku-buildpack-ruby.s3.amazonaws.com/cedar-14/ruby-2.1.7.tgz | tar
xz -C /app/heroku/ruby/ruby-2.1.7  
ENV PATH /app/heroku/ruby/ruby-2.1.7/bin:$PATH  
  
# Install Node  
RUN curl -s --retry 3 -L
http://s3pository.heroku.com/node/v0.12.7/node-v0.12.7-linux-x64.tar.gz | tar
xz -C /app/heroku/ruby/ && mv /app/heroku/ruby/node-v0.12.7-linux-x64
/app/heroku/ruby/node-0.12.7  
ENV PATH /app/heroku/ruby/node-0.12.7/bin:$PATH  
  
# Install Bundler  
RUN gem install bundler -v 1.9.10 \--no-ri \--no-rdoc  
ENV PATH /app/bin:/app/heroku/ruby/bundle/ruby/2.1.7/bin:$PATH  
ENV BUNDLE_APP_CONFIG /app/heroku/ruby/.bundle/config  
  
WORKDIR /app/user  

