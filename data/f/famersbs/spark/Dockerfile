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
  
# Install scala  
RUN apt-get install -y scala  
  
# Install Spark  
RUN curl -fL http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-
hadoop2.6.tgz | tar xzf - -C /opt && \  
mv /opt/spark-1.5.1-bin-hadoop2.6 /opt/spark  
  
# Install ssh  
RUN apt-get install -y ssh  
  
ADD run.sh run.sh

