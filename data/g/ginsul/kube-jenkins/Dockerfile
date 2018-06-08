FROM jenkins/jenkins:lts  
  
USER root  
  
  
RUN apt-get update  
RUN apt-get install -y \  
software-properties-common  
  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get update  
  
RUN apt-get install -y \  
maven \  
git  
  
RUN apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default  
  
RUN rm -rf /var/lib/apt/lists/*  

