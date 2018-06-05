FROM ubuntu:latest  
  
# install ruby  
RUN apt-get update  
RUN apt-get -y install build-essential  
  
RUN apt-get -y install software-properties-common  
RUN apt-add-repository ppa:brightbox/ruby-ng  
RUN apt-get update  
RUN apt-get -y install ruby1.9.3 ruby-switch  
  
RUN gem install bundler  
  
EXPOSE 11988  
RUN mkdir /mimicserver  
WORKDIR /mimicserver  
  
ADD ./Gemfile /mimicserver/Gemfile  
ADD ./mimic.rb /mimicserver/mimic.rb  
  
RUN bundle install  
  
RUN chmod 755 ./mimic.rb  
  
CMD ["./mimic.rb"]  

