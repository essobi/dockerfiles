FROM phylor/tomcat  
  
RUN rm -rf $CATALINA_HOME/webapps/*  
RUN wget -qO /tmp/piggydb.war
'http://downloads.sourceforge.net/project/piggydb/Piggydb/6.18/piggydb-6.18.war?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpiggydb%2Ffiles%2FPiggydb%2F6.18%2F&ts=1414792179&use_mirror=heanet'  
RUN unzip -d $CATALINA_HOME/webapps/ROOT /tmp/piggydb.war  
  
RUN sed -i 's/~\/piggydb/\/srv\/piggydb/' $CATALINA_HOME/webapps/ROOT/WEB-
INF/config/application.properties  
  
VOLUME /srv/piggydb  
  
CMD ["/srv/tomcat7/bin/catalina.sh", "run"]  

