FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.5.0  
RUN gem install circleci-bundle-update-pr --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["circleci-bundle-update-pr"]  
CMD ["--help"]  

