FROM java:8  
  
MAINTAINER Sjoerd Mulder <sjoerd@crobox.com>  
  
# EAP build number from
https://confluence.jetbrains.com/display/TW/Download+Latest  
ENV TEAMCITY_BUILD 41463  
  
ENV TEAMCITY_DATA_PATH /var/lib/teamcity  
# Get and install teamcity  
RUN wget -qO-
https://download.jetbrains.com/teamcity/eap/TeamCity-$TEAMCITY_BUILD.tar.gz |
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

