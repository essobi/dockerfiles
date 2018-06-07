FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN apt-get -y update  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install -y git  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN apt-get -y install oracle-java8-installer  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/bin  
RUN ln -s /usr/lib/jvm/java-8-oracle /usr/lib/jvm/default-java  
RUN apt-get -y install gradle  
RUN git clone https://github.com/robisrob/domygroceries.git  

