FROM ubuntu:14.04  
MAINTAINER usual2970 "536464346@qq.com"  
ENV REFRESHED_AT "2016-08-29"  
RUN apt-get -yqq update  
RUN apt-get -yqq install ruby ruby-dev make nodejs  
RUN gem install --no-rdoc --no-ri jekyll -v 2.5  
VOLUME /data  
VOLUME /var/www/html  
WORKDIR /data  
ENTRYPOINT ["jekyll","build","--destination=/var/www/html"]

