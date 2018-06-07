FROM ruby:2.2.3  
MAINTAINER pascal+docker@corpet.net  
  
RUN mkdir /test  
WORKDIR /test  
  
RUN gem install cucumber -v=2.3.2  
RUN gem install aruba -v=0.14.0  
  
CMD ["cucumber"]  

