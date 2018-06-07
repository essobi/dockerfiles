FROM java:8  
MAINTAINER Cesar Salazar <csalazar@devsu.com>  
  
# Update and install some utils  
RUN apt-get update \  
&& apt-get install -y tar software-properties-common libmysql-java \  
&& rm -rf /var/lib/apt/lists/*  
  
# Teamcity  
ENV TEAMCITY_DATA_PATH /data/teamcity  
ENV TEAMCITY_PACKAGE TeamCity-10.0.2.tar.gz  
ENV TEAMCITY_DOWNLOAD http://download.jetbrains.com/teamcity  
  
RUN wget $TEAMCITY_DOWNLOAD/$TEAMCITY_PACKAGE && \  
tar zxf $TEAMCITY_PACKAGE -C /opt && \  
rm -rf $TEAMCITY_PACKAGE  
  
# Adding symlink to the mysql driver  
RUN echo 'ln -sf /usr/share/java/mysql.jar /data/teamcity/lib/jdbc/mysql.jar'
>> /opt/TeamCity/bin/teamcity-init.sh  
  
EXPOSE 8111  
VOLUME ["/data/teamcity"]  
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]

