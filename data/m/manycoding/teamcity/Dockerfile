FROM java:8  
MAINTAINER Valery M. <vamukhs@gmail.com>  
  
ENV TEAMCITY_VERSION 10.0.2  
ENV TEAMCITY_DATA_PATH /var/lib/teamcity  
ENV TEAMCITY_SERVER http://localhost:8111  
  
# Install docker  
RUN apt-get update && apt-get install -y --no-install-recommends \  
docker.io \  
python-requests && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Get and install teamcity  
RUN wget -qO-
https://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.tar.gz |
tar xz -C /opt  
# Enable the correct Valve when running behind a proxy  
RUN sed -i -e "s/\\.*<\/Host>.*$/<Valve
className=\"org.apache.catalina.valves.RemoteIpValve\"
protocolHeader=\"x-forwarded-proto\" \/><\/Host>/"
/opt/TeamCity/conf/server.xml  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 8111  
  
VOLUME /var/lib/teamcity  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

