FROM ubuntu  
MAINTAINER Shaun Martin <shaun@samsite.ca>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
libffi-dev \  
make \  
ruby \  
ruby-dev \  
&& gem install fpm  
  
CMD ["/usr/local/bundle/bin/fpm", "--help"]  

