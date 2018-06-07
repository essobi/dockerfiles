FROM ruby:latest  
  
# Set the locale  
RUN apt-get update -qq && apt-get install -y locales -qq && locale-gen
en_US.UTF-8 en_us && locale-gen C.UTF-8 && /usr/sbin/update-locale
LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
RUN gem install middleman  
RUN gem install s3_website  
  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jre-headless  
RUN apt-get install -y nodejs  
  
VOLUME ["/website", "/config"]  
  
WORKDIR /website  
  
ENTRYPOINT ["s3_website"]  
  
CMD ["--help"]  

