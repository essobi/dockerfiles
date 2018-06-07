FROM ruby:2.1-onbuild  
MAINTAINER Jeremy Rice <jrice@eol.org>  
ENV LAST_FULL_REBUILD 2016-08-24  
RUN apt-get update -q && apt-get install libmagickwand-dev && apt-get clean
&&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN bundle install --without development test  
  
CMD /bin/bash  

