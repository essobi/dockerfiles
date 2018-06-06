FROM library/node:latest  
  
MAINTAINER Christian Ulbrich <christian.ulbrich@zalari.de>  
  
#install ruby  
RUN apt-get update && apt-get install -y ruby ruby-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#install latest compass  
RUN gem install compass

