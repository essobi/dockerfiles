FROM ruby:2.1  
ENV MAILCATCHER_VERSION 0.6.1  
RUN \  
gem install mailcatcher --no-ri --no-rdoc --version ${MAILCATCHER_VERSION}  
  
EXPOSE 1080  
EXPOSE 1025  
ENTRYPOINT [ "mailcatcher", "--ip=0.0.0.0", "--foreground" ]  

