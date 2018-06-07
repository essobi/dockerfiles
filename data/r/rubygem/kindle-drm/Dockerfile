FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.8.0  
RUN gem install kindle-drm --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["serial_to_pid.rb"]  
CMD ["--help"]  

