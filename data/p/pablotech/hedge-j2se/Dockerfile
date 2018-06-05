FROM pablotech/hedge-supervisord:latest  
  
# JAVA  
RUN sudo add-apt-repository -y ppa:webupd8team/java  
RUN sudo apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo
debconf-set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-
set-selections  
RUN sudo apt-get -y --force-yes --no-install-recommends install oracle-
java8-installer  
RUN sudo apt-get -y --force-yes --no-install-recommends install oracle-
java8-set-default  
RUN apt-get -y install oracle-java8-installer  

