FROM ubuntu:14.04  
RUN apt-get -y --force-yes update  
RUN apt-get -y --force-yes install ruby  
  
RUN gem install sinatra  
  
ADD . /opt/app  
  
WORKDIR /opt/app  
  
EXPOSE 4567  
VOLUME ["/opt/app"]  
  
CMD ruby hello.rb -o 0.0.0.0

