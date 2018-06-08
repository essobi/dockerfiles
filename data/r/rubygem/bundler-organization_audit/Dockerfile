FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.3.0  
RUN gem install bundler-organization_audit --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["bundle-organization-audit"]  
CMD ["--help"]  

