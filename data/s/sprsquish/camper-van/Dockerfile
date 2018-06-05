FROM ubuntu:12.04  
MAINTAINER Jeff Smick <jeff@squishtech.com>  
  
RUN apt-get update  
  
RUN apt-get install -y openssl  
RUN apt-get install -y ruby1.9.1  
RUN apt-get install -y build-essential  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y ruby1.9.1-dev  
  
RUN gem install --no-ri --no-rdoc -v 0.0.16 camper_van  
  
RUN apt-get remove -y build-essential  
RUN apt-get remove -y libssl-dev  
RUN apt-get remove -y ruby1.9.1-dev  
RUN apt-get autoremove -y  
  
RUN apt-get clean  
RUN gem source -c  
  
EXPOSE 7778  
ENTRYPOINT ["/usr/local/bin/camper_van"]  
CMD ["0.0.0.0", "7778", "--log-level=warn"]  

