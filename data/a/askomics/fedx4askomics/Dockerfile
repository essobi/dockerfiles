FROM maven:3.5.2-jdk-8-alpine  
MAINTAINER Olivier Filangi "olivier.filangi@inra.fr"  
COPY . /usr/local/fedx  
  
WORKDIR /usr/local/fedx  
RUN mvn clean dependency:copy-dependencies package  
  
CMD ["/usr/bin/java", "-d64", "-Xms2g", "-Xmx4g", "-cp",
"./target/fedx-0.0.1-SNAPSHOT-jar-with-dependencies.jar",
"fr.inra.igepp.askomics.HttpSimpleServer", "-e", "fedx", "-p", "4040"]  

