FROM vyolin/java7  
  
MAINTAINER Graham Taylor <gtayzlor@gmail.com>  
  
RUN wget http://ftp.fau.de/apache/maven/maven-3/3.3.1/binaries/apache-
maven-3.3.1-bin.tar.gz  
RUN tar -zxvf apache-maven-3.3.1-bin.tar.gz  
RUN rm apache-maven-3.3.1-bin.tar.gz  
RUN mv apache-maven-3.3.1 /usr/lib/mvn  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk  
ENV JAVA "$JAVA_HOME/bin"  
ENV M2_HOME /usr/lib/mvn  
ENV M2 "$M2_HOME/bin"  
ENV PATH "$PATH:$JAVA_HOME:$JAVA:$M2_HOME:$M2"  
ENV CLUSTER_URL http://127.0.0.1:8091  
  
COPY . /src  
WORKDIR /src  
  
CMD mvn -D com.couchbase.beersample.cluster=$CLUSTER_URL/pools jetty:run  

