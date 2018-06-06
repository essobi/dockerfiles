FROM ruby:latest  
MAINTAINER M Parker "mparker17@536298.no-reply.drupal.org"  
RUN gem update --system && \  
gem install compass  
  
VOLUME [ "/theme" ]  
WORKDIR "/theme"  
ENTRYPOINT [ "/usr/local/bundle/bin/compass" ]  
CMD [ "version" ]  

