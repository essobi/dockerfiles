FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.0.5  
RUN gem install codeclimate-test-reporter --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["cc-tddium-post-worker"]  
CMD ["--help"]  

