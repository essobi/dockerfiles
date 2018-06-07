FROM ubuntu:12.04  
MAINTAINER Ole Christian Langfjæran "judoole@gmail.com"  
RUN apt-get update && apt-get clean  
RUN apt-get install -q -y openjdk-7-jre-headless  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN apt-get clean  
RUN apt-get remove  
ADD
https://bintray.com/artifact/download/jfrog/artifactory/artifactory-3.8.0.zip
/tmp/artifactory.zip  
RUN unzip /tmp/artifactory.zip -d /  
RUN rm -rf /tmp/artifactory.zip  
RUN mv /artifactory-3.8.0 /artifactory  
  
VOLUME /artifactory/data  
VOLUME /artifactory/logs  
VOLUME /artifactory/backup  
  
EXPOSE 8081  
CMD ["/artifactory/bin/artifactory.sh"]  

