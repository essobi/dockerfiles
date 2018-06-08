FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.1.9  
RUN gem install foreverman-ar_mailer --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["ar_sendmail"]  
CMD ["--help"]  

