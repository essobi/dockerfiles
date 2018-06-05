FROM camstitt/python-deadsnakes  
  
RUN apt-get update -y  
RUN apt-get install -y m4 libpq-dev git libssl-dev libffi-dev build-essential
ruby-full rubygems make curl  
  
RUN gem install bundler  
RUN curl -sL https://deb.nodesource.com/setup_iojs_2.x | bash -  
RUN apt-get -y update  
RUN apt-get install -y iojs  

