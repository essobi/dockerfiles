FROM tutum/tomcat:7.0  
MAINTAINER Brett Antonides brett.antonides@lmnsolutions.com  
  
RUN apt-get update && apt-get install -y git maven  
  
RUN git clone https://github.com/Berico-Technologies/CLAVIN.git /clavin  
  
WORKDIR /clavin  
RUN wget -q http://download.geonames.org/export/dump/allCountries.zip && unzip
allCountries.zip  
RUN mvn compile  
RUN MAVEN_OPTS="-Xmx2048M" mvn exec:java
-Dexec.mainClass="com.bericotech.clavin.index.IndexDirectoryBuilder"  
RUN MAVEN_OPTS="-Xmx2048M" mvn exec:java
-Dexec.mainClass="com.bericotech.clavin.WorkflowDemo"  

