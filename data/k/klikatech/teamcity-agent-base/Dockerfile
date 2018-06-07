FROM java:openjdk-8-jdk  
  
MAINTAINER Eugene Volchek <evolchek@klika-tech.com>  
  
RUN groupadd -g 999 teamcity \  
&& useradd -u 999 -g teamcity -m teamcity \  
&& mkdir -p /opt/TeamCity && chown teamcity:teamcity /opt/TeamCity  
USER teamcity  
COPY runAgent /opt/TeamCity/  
VOLUME ["/home/teamcity"]  
CMD ["/opt/TeamCity/runAgent"]  

