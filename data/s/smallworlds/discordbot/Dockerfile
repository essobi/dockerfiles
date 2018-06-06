FROM ruby:latest  
MAINTAINER Lane Farrow "laneatomic@gmail.com"  
RUN apt-get update  
RUN apt-get install -y gcc g++ libsodium-dev ffmpeg ruby-dev libopus0 libffi-
dev libopus-dev  
RUN gem install bundler  
  
COPY . /project  
WORKDIR /project  
RUN bundle install  
  
CMD /project/run.sh  

