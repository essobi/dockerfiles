FROM evarga/jenkins-slave  
MAINTAINER Tian Lai <laitian912@gmail.com>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y \  
git \  
curl \  
unzip \  
software-properties-common  
  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install -y graphviz  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes oracle-java8-installer  
RUN mkdir /usr/java/ && ln -snf /usr/lib/jvm/java-8-oracle /usr/java/default  
  
USER jenkins  
RUN curl -s http://get.sdkman.io | bash && source
/home/jenkins/.sdkman/bin/sdkman-init.sh && yes|sdk install groovy 2.4.4  
USER root  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

