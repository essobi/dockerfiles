FROM ubuntu:14.04  
  
# http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html  
RUN sudo apt-get update  
RUN sudo apt-get install -y software-properties-common  
RUN sudo add-apt-repository ppa:webupd8team/java  
RUN sudo apt-get update  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y libjna-java oracle-java8-installer ca-certificates

