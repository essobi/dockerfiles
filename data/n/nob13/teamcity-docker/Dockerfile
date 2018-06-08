FROM java:8-jre  
  
MAINTAINER Norbert Schultz  
  
VOLUME ["/data/teamcity"]  
ENV TEAMCITY_DATA_PATH /data/teamcity  
  
RUN curl -L https://download.jetbrains.com/teamcity/TeamCity-9.1.7.tar.gz |
tar xz -C /opt  
  
# Note: we cannot download the Postgres (or other) database JDBC drivers so
easily because  
# Teamcity want's them inside the /data/teamcity/lib/jdbc directory.  
# but dockerfiles cannot write into directories which are supposed to be
exposed.  
# If you are creating a fresh new server, then you have to add this by hand  
# See:
https://confluence.jetbrains.com/display/TCD9/Setting+up+an+External+Database  
EXPOSE 8111  
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]  
  

