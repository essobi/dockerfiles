FROM ruby:2.4.0  
RUN mkdir -p /opt/valoration  
ADD . /opt/valoration  
WORKDIR /opt/valoration  
  
ENV VALORATION_MODE development  
  
RUN apt-get update  
RUN gem install bundler  
RUN bundle install  

