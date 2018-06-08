FROM ubuntu:trusty  
MAINTAINER fdot  
  
RUN apt-get update  
RUN apt-get install -y build-essential software-properties-common  
RUN add-apt-repository ppa:brightbox/ruby-ng  
RUN apt-get update  
RUN apt-get install -y ruby2.3 ruby2.3-dev zlib1g-dev  
RUN gem install --no-ri --no-rdoc bundler  
RUN mkdir /app  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle config --global silence_root_warning 1  
WORKDIR /app  
RUN gem install pygments.rb  
RUN bundle install  
RUN mkdir /working_dir  
WORKDIR /app/working_dir  
RUN bundle install  
  
VOLUME ["/app/working_dir"]  
  
EXPOSE 4567  
CMD ["bundle", "exec", "middleman", "server"]

