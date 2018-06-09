FROM streamsets/datacollector:2.7.2.0  
ARG ADD_LIBS=streamsets-datacollector-elasticsearch_5-lib,streamsets-
datacollector-jdbc-lib,streamsets-datacollector-jython_2_7-lib  
  
RUN if [[ ! -z $ADD_LIBS ]]; then $SDC_DIST/bin/streamsets stagelibs
-install=$ADD_LIBS ; fi  
  
USER root  
COPY docker-entrypoint.sh /  
RUN ["chmod", "+x", "/docker-entrypoint.sh"]  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["dc", "-exec"]  

