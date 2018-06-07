FROM niro/spark-r  
  
MAINTAINER Nirosan <pnirosan@gmail.com>  
  
ENV MAVEN_VERSION 3.3.9  
RUN curl -sSL
http://mirror.nus.edu.sg/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_OPTS="-Xmx512m -XX:MaxPermSize=128m"  
RUN apt-get -y update && apt-get -y install \  
npm  
  
RUN git clone https://github.com/elbamos/Zeppelin-With-R.git  
  
ADD build_mvn.sh /usr/local/bin/build_mvn.sh  
ADD scripts/start-script.sh /start-script.sh  
  
RUN /usr/local/bin/build_mvn.sh  
  
EXPOSE 8080 8081  
CMD ["/start-script.sh"]  

