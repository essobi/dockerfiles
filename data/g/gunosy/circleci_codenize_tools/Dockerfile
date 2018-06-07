FROM circleci/ruby:2.2.7  
WORKDIR /root/  
ADD work work  
  
COPY work/Gemfile $WORKDIR  
RUN sudo apt-get update && sudo apt-get upgrade -y  
RUN sudo apt-get install -y libpcap-dev  
  
WORKDIR /root/work/  
RUN sudo gem update  
RUN sudo bundle install  

