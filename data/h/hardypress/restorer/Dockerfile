FROM starefossen/ruby-node:2-8  
MAINTAINER Claudio Benvenuti <claudio@hardypress.com>  
RUN apt-get update && apt-get install -y awscli curl ssed locales && localedef
-i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
RUN echo 'LC_ALL=en_US.UTF-8\n\  
LANGUAGE en_US:en\n\  
LANG=en_US.UTF-8' >> /etc/environment  
RUN apt-get install -y openjdk-8-jre-headless  
RUN gem install s3_website  
RUN s3_website install  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  

