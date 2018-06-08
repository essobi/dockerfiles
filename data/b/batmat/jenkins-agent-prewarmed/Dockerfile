FROM java:8  
MAINTAINER Baptiste <batmat> Mathus  
  
RUN wget http://apache.crihan.fr/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.zip  
RUN unzip apache-maven-3.3.9-bin.zip  
RUN ls  
RUN mkdir -p /jenkins/tools/hudson.tasks.Maven_MavenInstallation/  
RUN mv apache-maven-3.3.9
/jenkins/tools/hudson.tasks.Maven_MavenInstallation/mvn-3.3.9/  
  
ENV PATH
/jenkins/tools/hudson.tasks.Maven_MavenInstallation/mvn-3.3.9/bin:$PATH  
  
WORKDIR /tmp  
  
RUN git clone https://github.com/jenkinsci/jenkins  
  
WORKDIR jenkins  
RUN mvn clean install -DskipTests  

