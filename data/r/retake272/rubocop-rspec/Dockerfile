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
ARG rubocop_version=0.53.0  
ARG rubocop_rspec_version=1.25.1  
RUN gem install rubocop -v ${rubocop_version}  
RUN gem install rubocop-rspec -v ${rubocop_rspec_version}  
  
WORKDIR /app  
VOLUME /app  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

