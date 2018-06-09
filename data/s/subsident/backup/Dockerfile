FROM ruby:2.1-wheezy  
MAINTAINER SHS  
RUN apt-get update \  
&& apt-get install -y mysql-client-5.5 \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem install backup  

