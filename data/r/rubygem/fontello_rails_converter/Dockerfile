FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.4.6  
RUN gem install fontello_rails_converter --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["fontello"]  
CMD ["--help"]  

