FROM ubuntu:16.04  
MAINTAINER "jocag@uma.es"  
RUN apt-get -y update  
RUN apt-get -y install ruby ruby-dev sudo build-essential git  
RUN apt-get clean  
  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN sudo sh -c 'echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config'  
  
RUN gem install puppet -v 4.7.1  
RUN gem install librarian-puppet -v 2.2.3  
RUN gem install puppet-parse -v 0.1.4  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set up the volumes and working directory  
VOLUME ["/puppet"]  
WORKDIR /puppet  
  
ENTRYPOINT ["librarian-puppet"]  
CMD ["install"]  

