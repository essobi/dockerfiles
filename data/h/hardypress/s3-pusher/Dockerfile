FROM ruby:2-stretch  
MAINTAINER Claudio Benvenuti <claudio@hardypress.com>  
RUN apt-get update && apt-get install -y openjdk-8-jre-headless locales &&
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8  
RUN echo 'LC_ALL=en_US.UTF-8\n\  
LANGUAGE en_US:en\n\  
LANG=en_US.UTF-8' >> /etc/environment  
ENV LANG C.UTF-8  
RUN gem install s3_website  
RUN s3_website install  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  

