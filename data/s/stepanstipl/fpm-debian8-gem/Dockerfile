FROM debian:jessie  
MAINTAINER Stepan Stipl  
# https://github.com/stepanstipl/  
RUN apt-get update \  
&& apt-get install -y ruby ruby-dev gcc make \  
&& rm -rf /var/lib/apt/lists/*  
RUN gem install fpm  
  
RUN mkdir /output  
WORKDIR /output  
  
ENV DEB_PREFIX rubygem  
ENV DEPENDENCIES false  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

