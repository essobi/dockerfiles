FROM developerinlondon/ruby-mri:2.1.2  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev
libsqlite3-dev  
RUN mkdir /myapp  
WORKDIR /myapp  
ADD Gemfile /myapp/Gemfile  
RUN bundle install  
ADD . /myapp  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

