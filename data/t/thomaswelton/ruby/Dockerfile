FROM thomaswelton/ubuntu  
  
MAINTAINER thomaswelton  
  
# Ruby  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-software-
properties  
RUN apt-add-repository ppa:brightbox/ruby-ng  
RUN apt-get -qq update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ruby2.0 ruby2.0-dev
rubygems ruby-switch  
RUN ruby-switch --set ruby2.0  
  
RUN gem install rake bundler --no-rdoc --no-ri  
  
RUN apt-get remove -y python-software-properties  

