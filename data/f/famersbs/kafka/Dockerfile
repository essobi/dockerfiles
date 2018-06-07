FROM famersbs/delauncher_base  
MAINTAINER Sean <famersbs@gmail.com>  
  
# install oracle java  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
RUN add-apt-repository ppa:webupd8team/java -y  
  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
RUN apt-get install -y oracle-java7-installer  
  
# Install Spark  
RUN curl -fL
http://mirror.cc.columbia.edu/pub/software/apache/kafka/0.8.2.1/kafka_2.11-0.8.2.1.tgz
| tar xzf - -C /opt && \  
mv /opt/kafka_2.11-0.8.2.1 /opt/kafka  
  
ADD run.sh run.sh

