FROM ruby:2.3  
MAINTAINER "Matsuura Keita<retake272@gmail.com>"  
# locale  
RUN apt-get update  
RUN apt-get install locales -y  
RUN echo "ja_JP UTF-8" > /etc/locale.gen  
RUN locale-gen  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ARG rubycritic_version=3.4.0  
RUN gem install -N rubycritic -v ${rubycritic_version}  
  
WORKDIR /app  
VOLUME /app  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

