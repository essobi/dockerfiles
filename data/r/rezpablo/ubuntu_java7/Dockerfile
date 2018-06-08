FROM rezpablo/ubuntu_dev  
  
MAINTAINER rezpablo@gmail.com  
  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java7-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  

