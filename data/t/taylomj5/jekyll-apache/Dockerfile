FROM ubuntu:14.04  
MAINTAINER Matthew Taylor <taylomj5@student.op.ac.nz>  
ENV REFRESHED_AT 2014-06-01  
RUN apt-get -yqq update  
RUN apt-get -yqq install ruby ruby-dev make nodejs  
RUN gem install --no-rdoc --no-ri jekyll  
  
VOLUME ["/data/","/var/www/html"]  
WORKDIR /data  
  
ENTRYPOINT ["jekyll","build","--destination=/var/www/html"]  
  

