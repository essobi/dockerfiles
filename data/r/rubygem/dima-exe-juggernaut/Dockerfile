FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.5.9.26  
RUN gem install dima-exe-juggernaut --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["juggernaut"]  
CMD ["--help"]  

