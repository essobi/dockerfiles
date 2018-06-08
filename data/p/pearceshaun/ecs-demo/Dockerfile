FROM ubuntu:latest  
MAINTAINER Shaun Pearce <sppearce@amazon.com>  
  
# Packages  
RUN apt-get update && apt-get install -y ruby ruby-dev  
  
# Gems  
RUN gem install sinatra  
RUN gem install sinatra-contrib  
RUN gem install redis  
#RUN gem install aws-sdk --pre  
RUN mkdir /app  
  
EXPOSE 5000  
COPY app /app/  
#COPY credentials ~/.aws/credentials  
CMD ruby /app/app.rb -p 5000

