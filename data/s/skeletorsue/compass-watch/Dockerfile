FROM ruby:latest  
MAINTAINER Chris Staley "skeletorsue@gmail.com"  
RUN gem update --system  
RUN gem install compass  
RUN gem install sass  
RUN gem install susy  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
VOLUME [ "/theme" ]  
WORKDIR "/theme"  
ENTRYPOINT [ "/usr/local/bundle/bin/compass" ]  
CMD [ "watch" ]  

