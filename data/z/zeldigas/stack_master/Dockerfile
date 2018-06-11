FROM ruby:2.2.6-slim  
MAINTAINER Dmitry Pavlov <zeldigas@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y build-essential \  
&& gem install --no-rdoc --no-ri stack_master \  
&& apt-get remove -y build-essential \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt /var/lib/dpkg /var/cache/*  
  
RUN mkdir /conf  
  
WORKDIR /conf  
VOLUME ["/conf"]  
  
ENTRYPOINT ["stack_master"]

