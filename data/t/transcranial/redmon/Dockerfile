FROM debian:jessie  
  
RUN apt-get update -qq  
  
RUN apt-get install ruby ruby-dev build-essential --no-install-recommends -qqy  
  
ADD https://rubygems.org/rubygems/rubygems-2.6.10.tgz /  
  
RUN tar xvf /rubygems-2.6.10.tgz && cd /rubygems-2.6.10 && ruby setup.rb  
  
RUN gem install redmon  
  
EXPOSE 4567  
ENTRYPOINT ["redmon"]  

