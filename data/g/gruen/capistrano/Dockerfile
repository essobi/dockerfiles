FROM ruby:2.2-alpine  
  
LABEL maintainer "Darren Green <darren@gruen.site>"  
  
WORKDIR /app  
  
VOLUME ["/app"]  
  
CMD ["cap"]  
  
ENTRYPOINT ["cap"]  
  
RUN gem install capistrano --version=3.5.0  
  

