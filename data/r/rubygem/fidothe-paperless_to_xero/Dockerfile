FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.1.1  
RUN gem install fidothe-paperless_to_xero --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["paperless_to_xero"]  
CMD ["--help"]  

