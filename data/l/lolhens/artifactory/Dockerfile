FROM lolhens/baseimage-oraclejdk:latest  
MAINTAINER LolHens <pierrekisters@gmail.com>  
  
  
ENV ARTIFACTORY_VERSION 6.0.1  
ENV ARTIFACTORY_NAME artifactory-oss-$ARTIFACTORY_VERSION  
ENV ARTIFACTORY_FILE jfrog-$ARTIFACTORY_NAME.zip  
ENV ARTIFACTORY_URL
https://bintray.com/artifact/download/jfrog/artifactory/$ARTIFACTORY_FILE  
ENV ARTIFACTORY_HOME /usr/local/artifactory  
  
  
RUN cd "/tmp" \  
&& curl -LO $ARTIFACTORY_URL \  
&& unzip $ARTIFACTORY_FILE \  
&& mv $ARTIFACTORY_NAME $ARTIFACTORY_HOME \  
&& cleanimage  
  
RUN appfolders add "artifactory/data" "$ARTIFACTORY_HOME/data" \  
&& appfolders add "artifactory/access" "$ARTIFACTORY_HOME/access" \  
&& appfolders add "artifactory/etc" "$ARTIFACTORY_HOME/etc" \  
&& appfolders add "artifactory/logs" "$ARTIFACTORY_HOME/logs" \  
&& appfolders add "artifactory/backup" "$ARTIFACTORY_HOME/backup"  
  
WORKDIR $ARTIFACTORY_HOME  
CMD bin/artifactory.sh  
  
VOLUME /usr/local/appdata/artifactory  
  
EXPOSE 8081  

