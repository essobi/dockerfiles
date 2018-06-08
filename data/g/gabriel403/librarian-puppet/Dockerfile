FROM ubuntu:16.04  
RUN apt-get -y update  
RUN apt-get -y install rubygems || apt-get -y install ruby ruby-dev  
RUN apt-get -y install build-essential git  
RUN apt-get clean  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN gem install puppet librarian-puppet  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set up the volumes and working directory  
VOLUME ["/puppet"]  
WORKDIR /puppet  
  
CMD librarian-puppet install

