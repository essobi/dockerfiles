FROM lonefreak/jenkins-slave-base  
MAINTAINER Fabricio Leotti <fabricio.lotti@gmail.com>  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/jre  
  
RUN apt-get update && apt-get install -y build-essential git && apt-get clean  
RUN wget
http://mirror.cc.columbia.edu/pub/software/apache/maven/maven-3/3.0.5/binaries/apache-
maven-3.0.5-bin.tar.gz \  
&& tar xzf apache-maven-3.0.5-bin.tar.gz -C /usr/local \  
&& cd /usr/local \  
&& ln -s apache-maven-3.0.5 maven \  
&& ln -s /usr/local/maven/bin/mvn /usr/local/bin/mvn  
RUN mkdir -p ~/.ssh  
ADD desc.sh /desc.sh  
ADD id_rsa /home/jenkins/.ssh/id_rsa  
ADD id_rsa.pub /home/jenkins/.ssh/id_rsa.pub  
RUN chmod 777 /desc.sh \  
&& chmod 600 /home/jenkins/.ssh/id_rsa /home/jenkins/.ssh/id_rsa.pub  
CMD []

