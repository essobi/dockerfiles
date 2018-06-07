FROM hipflat/rbenv:ruby-2.1.2  
MAINTAINER Roonglit Chareonsupkul <roonglit@gmail.com>  
  
# install dependencies  
RUN apt-get install -qy supervisor monit postfix  
  
# install Javascript Runtime  
RUN apt-get update  
RUN apt-get install -qy nodejs  
  
# set up monit configuration  
ADD ./monitrc /etc/monit/monitrc  
RUN chmod 700 /etc/monit/monitrc  
  
# add configuration for postfix  
RUN echo "master.hipflat.co.th" > /etc/mailname  
ADD ./postfix_main.cf /etc/postfix/main.cf  
  
# set up app folder  
WORKDIR /app  
RUN mkdir /app/log  
RUN mkdir -p /app/tmp/pids  
  
# adding Gemfile and Gemfile.lock to bundle install libraries  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
RUN bundle install --without development test  
  
ENV RAILS_ENV production  
  

