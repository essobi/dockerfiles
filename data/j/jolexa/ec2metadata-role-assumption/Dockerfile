FROM ruby:2.1  
RUN apt-get update  
RUN apt-get install -y python-pip python-dev  
RUN pip install --upgrade awscli  
ADD ./Gemfile /code/Gemfile  
ADD ./Gemfile.lock /code/Gemfile.lock  
WORKDIR /code  
RUN bundle install  
ADD . /code  
CMD bundle exec ruby ./ec2metadata.rb  

