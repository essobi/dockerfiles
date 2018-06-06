FROM oracle/openjdk:8  
MAINTAINER Sergio De Lorenzis <sergio.delorenzis@albaproject.it>  
  
ENV M2_HOME /usr/local/maven  
ENV PATH=${M2_HOME}/bin:${PATH}  
ENV MAVEN_VERSION=3.3.9  
ENV BASE_DIR=/opt/css-am  
  
RUN yum install wget tar -y; \  
wget http://apache.panu.it/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz; \  
tar xzf apache-maven-$MAVEN_VERSION-bin.tar.gz -C /usr/local; \  
cd /usr/local; \  
ln -s apache-maven-$MAVEN_VERSION maven;  
  
  
RUN cd /opt; mkdir css-am;  
  
COPY / $BASE_DIR  
  
RUN cd $BASE_DIR; mvn clean package -DskipTests=true; mv target/css-am*.jar
./app.jar;  
  
EXPOSE 80  
WORKDIR $BASE_DIR  
  
ENTRYPOINT ["java", "-jar", "app.jar"]  

