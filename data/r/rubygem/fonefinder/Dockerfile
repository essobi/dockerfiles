FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.0.3  
RUN gem install FoneFinder --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["FoneFinderTest.rb"]  
CMD ["--help"]  

