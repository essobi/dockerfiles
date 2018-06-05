FROM ubuntu:14.04  
MAINTAINER Albert Alvarez  
  
  
# Install  
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget  
RUN apt-get install software-properties-common -y  
#RUN add-apt-repository ppa:openjdk-r/ppa  
#RUN apt-get update  
#RUN apt-get install -y openjdk-8-jre openjdk-8-jdk  
#RUN apt-get update  
RUN apt-get install -y python-software-properties debconf-utils  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | sudo debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
  
  
RUN add-apt-repository ppa:ubuntu-desktop/ubuntu-make -y  
RUN apt-get update && apt-get install ubuntu-make -y  
RUN umake ide eclipse /root/.local/share/umake/ide/eclipse  
  
  
ENTRYPOINT ["/root/.local/share/umake/ide/eclipse/eclipse"]  

