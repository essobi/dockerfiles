FROM ubuntu:wily  
MAINTAINER sammy8806  
  
RUN apt-get update; apt-get upgrade -y  
RUN apt-get install -y build-essential  
RUN apt-get install -y git subversion  
RUN apt-get install -y cmake  
  
# Dependencies  
RUN apt-get install -y libboost-all-dev  
RUN apt-get install -y libcurl3-openssl-dev  
RUN apt-get install -y openssl  
RUN apt-get install -y libssl-dev  
RUN apt-get build-dep -y openssl  
  
# colorize output of make  
RUN apt-get install -y colormake  
RUN echo "alias make='colormake '\n" >> /etc/bash.bashrc  
  
CMD ["/bin/bash"]  

