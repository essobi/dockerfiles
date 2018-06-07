FROM greatfox/ssh  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN apt-get -y install oracle-java8-installer  
RUN ln -s /usr/lib/jvm/java-8-oracle /usr/lib/jvm/default-java  

