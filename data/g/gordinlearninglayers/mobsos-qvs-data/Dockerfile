FROM learninglayers/base  
  
MAINTAINER Dominik Renzel  
  
# add content to data volumes  
ADD etc /opt/mobsos-query-visualization/etc  
  
# provide directory as volume  
VOLUME ["/opt/mobsos-query-visualization/etc/"]  
  
# do necessary replacements by environment variable values (  
CMD sed -i "s#LAYERS_API_URI#${LAYERS_API_URI}#g" /opt/mobsos-query-
visualization/etc/i5.las2peer.webConnector.WebConnector.properties && \  
sed -i "s#LAYERS_API_URI#${LAYERS_API_URI}#g" /opt/mobsos-query-
visualization/etc/i5.las2peer.services.queryVisualization.QueryVisualizationService.properties
&& \  
sed -i "s#QVS_DB_NAME#${QVS_DB_NAME}#g" /opt/mobsos-query-
visualization/etc/i5.las2peer.services.queryVisualization.QueryVisualizationService.properties
&& \  
sed -i "s#QVS2_DB_NAME#${QVS2_DB_NAME}#g" /opt/mobsos-query-
visualization/etc/i5.las2peer.services.queryVisualization.QueryVisualizationService.properties
&& \  
sed -i "s#SERVICE_OIDC_CLIENT_ID#${SERVICE_OIDC_CLIENT_ID}#g" /opt/mobsos-
query-
visualization/etc/i5.las2peer.services.queryVisualization.QueryVisualizationService.properties
&& \  
sed -i "s#SERVICE_APIURL#${SERVICE_APIURL}#g" /opt/mobsos-query-
visualization/etc/i5.las2peer.services.queryVisualization.QueryVisualizationService.properties  

