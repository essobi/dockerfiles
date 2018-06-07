FROM java:openjdk-8  
MAINTAINER nils.kuhn@iteratec.de, birger.kamp@iteratec.de  
  
ENV OSM_DA_VERSION 1.0.0  
ENV OSM_DA_HOME /osm_da  
ENV OSM_DA_CONFIG_HOME /home/osm_da/.grails  
ENV JAVA_OPTS "-server -Dgrails.env=prod -Dfile.encoding=UTF-8"  
ENV DOCKERIZE_VERSION v0.2.0  
# add osm_da-user  
RUN useradd -ms /bin/bash osm_da  
  
# install dockerize  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# get osm_da-sources and build war-file  
RUN mkdir -p $OSM_DA_HOME $OSM_DA_HOME/logs $OSM_DA_CONFIG_HOME  
WORKDIR $OSM_DA_HOME  
ADD ./build/libs/OsmDetailAnalysis*.war $OSM_DA_HOME/OsmDetailAnalysis.war  
  
# add osm_da config file  
ADD ./docker/templates/osm_da-config.yml.j2
$OSM_DA_CONFIG_HOME/OsmDetailAnalysis-config.yml.j2  
  
# add entrypoint script  
ADD ./docker/entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh && \  
chown osm_da:osm_da -R $OSM_DA_HOME $OSM_DA_CONFIG_HOME  
  
USER osm_da  
VOLUME ["${OSM_DA_CONFIG_HOME}", "${OSM_DA_HOME}/logs"]  
EXPOSE 8081  
ENTRYPOINT dockerize -template ${OSM_DA_CONFIG_HOME}/OsmDetailAnalysis-
config.yml.j2:${OSM_DA_CONFIG_HOME}/OsmDetailAnalysis-config.yml \  
-stdout ${OSM_DA_HOME}/logs/OsmDetailAnalysisDetails.log -stderr ${OSM_DA_HOME}/logs/OsmDetailAnalysis.log \  
/entrypoint.sh  

