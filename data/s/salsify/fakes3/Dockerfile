FROM ruby:2.2-alpine  
  
RUN apk add --no-cache git  
  
RUN git clone https://github.com/salsify/fake-s3.git /opt/fakes3  
  
WORKDIR /opt/fakes3  
  
RUN bundle install  
  
EXPOSE 4554  
CMD ["/opt/fakes3/bin/fakes3", "-r", "/var/data/fakes3", "-p", "4554", "-h",
"fakes3"]  

