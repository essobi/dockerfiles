FROM ruby:2.3  
MAINTAINER labs.garsue@gmail.com  
  
ENV ULTRAHOOK_VERSION 0.1.4  
RUN gem install ultrahook -v $ULTRAHOOK_VERSION  
  
ADD ./ultrahook.bash /usr/bin/  
  
ENTRYPOINT ["/usr/bin/ultrahook.bash"]  

