FROM ubuntu:14.04  
# set all env variables  
ENV ZK zookeeper:2181  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV CLUSTER supercluster_v6  
ENV CONTROLLER helix_1  
ENV MODE STANDALONE  
  
# install tools get needed software  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common wget  
  
# add repo for oracle jdk  
RUN add-apt-repository -y ppa:webupd8team/java  
  
# set flag that license is agreed to  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
  
# install oracle jdk7  
RUN apt-get update && apt-get install -y oracle-java7-installer  
  
# copy init script over  
ADD src /util  
  
# create directories to download helix  
RUN mkdir -p /helix/helix-core  
RUN wget -O /helix/helix-core.tar
http://www.carfab.com/apachesoftware/helix/0.6.4/binaries/helix-
core-0.6.4-pkg.tar  
RUN tar xf /helix/helix-core.tar -C /helix/helix-core --strip-components=1  
WORKDIR /util  
CMD ./helix-init.sh  

