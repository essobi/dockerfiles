FROM billyboingo/docker-oracle-jdk:java8  
MAINTAINER Bill Weiss <billyboingo@gmail.com>  
  
#Install the tools we will need  
RUN apt-get -q update && apt-get install -qy --force-yes \  
curl \  
wget \  
unzip  
  
#Download and install latest Artifactory  
ENV ARTIFACTORY_VERSION 5.6.1  
ENV ARTIFACTORY_NAME artifactory-oss-$ARTIFACTORY_VERSION  
ENV ARTIFACTORY_FILE jfrog-$ARTIFACTORY_NAME.zip  
ENV ARTIFACTORY_URL
https://bintray.com/artifact/download/jfrog/artifactory/$ARTIFACTORY_FILE  
  
RUN wget -nv -P /tmp $ARTIFACTORY_URL  
RUN unzip /tmp/$ARTIFACTORY_FILE -d /tmp && \  
mv /tmp/$ARTIFACTORY_NAME/* /app  
  
#Clean up  
RUN apt-get -y autoremove; apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
#Adding Custom files  
COPY services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run  
  
#Mappings and Ports  
VOLUME ["/app/data","/app/backup","/app/logs","/app/etc"]  
EXPOSE 8081

