  
# docker run -dt -p 8111:8111 kornsn/centos7-teamcity-server  
FROM kornsn/centos7-oracle-jre7  
  
MAINTAINER Sergei Korneev <Sergei_Korneev@epam.com>  
  
# TeamCity data is stored in a volume to facilitate container upgrade  
VOLUME ["/data/teamcity"]  
ENV TEAMCITY_DATA_PATH /data/teamcity  
  
# Download and install TeamCity to /opt  
RUN yum -y install tar wget  
ENV TEAMCITY_PACKAGE TeamCity-9.0.3.tar.gz  
ENV TEAMCITY_DOWNLOAD http://download-cf.jetbrains.com/teamcity  
RUN wget --progress=bar:force -O- $TEAMCITY_DOWNLOAD/$TEAMCITY_PACKAGE | tar
xz --directory=/opt  
  
EXPOSE 8111  
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]  

