FROM debian  
MAINTAINER nise_nabe <nise.nabe@gmail.com>  
  
RUN apt-get -qq update && apt-get -y upgrade && apt-get clean  
  
RUN apt-get install -y rubygems libsqlite3-dev  
RUN gem install mailcatcher --no-ri --no-rdoc  
  
EXPOSE 1080  
EXPOSE 25  
CMD mailcatcher --smtp-port 25 --ip `ip addr show dev eth0 scope global | grep
inet | awk '{print $2;}' | cut -d/ -f1` -f  

