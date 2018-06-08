FROM ubuntu:16.04  
# Update Package Repos  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
  
# Install Java  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN apt-get install -y oracle-java8-installer  
RUN apt-get install -y oracle-java8-set-default  
  
RUN apt-get install unzip  
  
# Install Scala  
RUN wget -O /tmp/activator.zip https://downloads.typesafe.com/typesafe-
activator/1.3.12/typesafe-activator-1.3.12-minimal.zip && unzip
/tmp/activator.zip -d /usr/lib/activator  
RUN ln -s /usr/lib/activator/activator-1.3.12-minimal/bin/activator
/usr/local/bin/activator  

