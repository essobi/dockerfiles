FROM ruby:2.3.1  
MAINTAINER Guillermo Guerrero 'guillermo.guerrero@fr.fcm.travel'  
  
RUN apt-get update -qq && apt-get upgrade -y && apt-get install -y build-
essential libsnappy-dev libpq-dev cron libicu-dev  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && apt-get install
-y nodejs  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

