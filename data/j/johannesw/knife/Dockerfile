FROM ubuntu  
  
MAINTAINER Johannes Wettinger, http://github.com/jojow  
  
  
  
RUN apt-get -y update && apt-get -y install curl  
  
RUN curl -L https://www.opscode.com/chef/install.sh | bash  
  
WORKDIR /  
  
RUN mkdir .chef  
RUN echo "log_level :info" >> .chef/knife.rb  
RUN echo "log_location STDOUT" >> .chef/knife.rb  
  
ENTRYPOINT [ "knife" ]  

