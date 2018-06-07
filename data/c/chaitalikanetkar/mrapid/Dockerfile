FROM jenkins:1.609.1  
MAINTAINER Chaitali Kanetkar  
  
WORKDIR /mRapidMFToHadoop  
  
# Update the repositories and then install java  
#RUN apt-get update && install -y default-jre  
# Copy the application from its folder to our image  
# Assumes docker build is run from /myapp/src  
#ADD
/var/lib/jenkins/workspace/Data_Ingestion/target/mRapidMFToHadoop-0.0.1-SNAPSHOT.jar
/home/bigdata_coe/chaitali_workspace/jar  
#ADD /mRapidMFToHadoop/target/mRapidMFToHadoop-0.0.1-SNAPSHOT.jar
mRapidMFToHadoop-0.0.1-SNAPSHOT.jar  
# Run the app when the container is executed.  
#CMD ["java", "-jar mRapidMFToHadoop-0.0.1-SNAPSHOT.jar"]  
EXPOSE 4567  
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar",
"target/mRapidMFToHadoop-0.0.1-SNAPSHOT.jar"]  

