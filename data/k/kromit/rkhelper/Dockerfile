FROM openjdk:alpine  
RUN wget http://www-us.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
RUN tar -zxvf apache-maven-3.3.9-bin.tar.gz  
RUN rm apache-maven-3.3.9-bin.tar.gz  
RUN mv apache-maven-3.3.9 /usr/lib/mvn  
  
#ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk  
#ENV JAVA=$JAVA_HOME/bin  
ENV M2_HOME=/usr/lib/mvn  
ENV M2=$M2_HOME/bin  
ENV PATH $PATH:$M2_HOME:$M2  
  
COPY regkassen-common/ /usr/src/regkasse/regkassen-common/  
WORKDIR /usr/src/regkasse/regkassen-common  
RUN mvn install  
  
COPY regkassen-core/ /usr/src/regkasse/regkassen-core/  
WORKDIR /usr/src/regkasse/regkassen-core  
RUN mvn install  
  
WORKDIR /usr/src/regkasse/regkassen-core/target/  
CMD ["java","-jar","registrierkassen-core-0.7.1.jar"]  

