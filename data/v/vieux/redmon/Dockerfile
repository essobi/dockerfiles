FROM debian:jessie  
  
RUN apt-get update -qq  
  
RUN apt-get install ruby ruby-dev build-essential --no-install-recommends -qqy  
  
ADD http://production.cf.rubygems.org/rubygems/rubygems-2.2.2.tgz /  
  
RUN tar xvf /rubygems-2.2.2.tgz && cd /rubygems-2.2.2 && ruby setup.rb  
  
RUN gem install redmon  
  
EXPOSE 4567  
ENTRYPOINT ["redmon"]  

