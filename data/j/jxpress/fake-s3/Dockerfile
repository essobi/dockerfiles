FROM ruby:2.3.1-alpine  
  
ENV FAKES3_VERSION 0.2.4  
RUN mkdir /data  
RUN gem install fakes3 -v $FAKES3_VERSION  
  
EXPOSE 4567  
ENTRYPOINT ["fakes3"]  
  
CMD ["-r", "/data", "-p", "4567"]  

