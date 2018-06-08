FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=4.0.2  
RUN gem install flame_channel_parser --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["bake_flame_channel"]  
CMD ["--help"]  

