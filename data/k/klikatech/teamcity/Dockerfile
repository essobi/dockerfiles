FROM java:openjdk-8-jre  
  
MAINTAINER Eugene Volchek <evolchek@klika-tech.com>  
  
ENV TEAMCITY_VERSION 10.0.3  
VOLUME ["/var/lib/teamcity"]  
RUN mkdir -p /var/lib/teamcity \  
&& groupadd -g 999 teamcity \  
&& useradd -u 999 -g teamcity -d /var/lib/teamcity teamcity \  
&& chown -R teamcity:teamcity /var/lib/teamcity \  
&& wget -qO-
http://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.tar.gz | tar
xz -C /opt \  
&& chown -R teamcity:teamcity /opt/TeamCity  
USER teamcity  
EXPOSE 8111  
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]  

