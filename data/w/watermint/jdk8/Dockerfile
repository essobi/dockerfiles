#  
# JDK 8  
#  
FROM watermint/base  
MAINTAINER Takayuki Okazaki (https://hub.docker.com/u/watermint/)  
  
RUN apt-get install -y software-properties-common  
  
# JDK  
# -----  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get update  
RUN apt-get install -y oracle-java8-installer  
RUN apt-get install -y oracle-java8-set-default  

