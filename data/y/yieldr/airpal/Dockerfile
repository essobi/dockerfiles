FROM java:8  
MAINTAINER Georgios Georgiadis <georgios.georgiadis@yieldr.com>  
  
RUN apt-get update && \  
apt-get install -y g++ mysql-client make  
  
# Install gradle  
RUN wget https://services.gradle.org/distributions/gradle-2.4-bin.zip  
RUN unzip gradle-2.4-bin.zip  
ENV PATH /gradle-2.4-bin/bin:$PATH  
  
# wget airpal, det dir: airpal-master  
RUN wget https://github.com/airbnb/airpal/archive/master.zip -O airpal.zip  
RUN unzip airpal.zip -d /  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
WORKDIR /airpal-master  
RUN bash gradlew clean shadowJar  
  
# AIRPAL_DB_NAME/PRESTO_COORDINATOR_URL will disable when bind mount /airpal-
master/reference.yml  
# ENV AIRPAL_DB_NAME airpal  
# ENV PRESTO_COORDINATOR_URL http://10.8.1.9:8080  
EXPOSE 8081 8082  
# using ENV or bind mount /airpal-master/reference.yml before run.sh  
CMD ["/run.sh"]

