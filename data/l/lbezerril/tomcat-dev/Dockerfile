FROM tomcat:8.5.8-jre8  
  
# Adiciona o atributo reloadable="true" na tag <Context> do arquivo  
# $CATALINA_HOME/conf/context.xml via comando sed.  
RUN sed -i 's/<Context>/<Context reloadable="true">/g' \  
$CATALINA_HOME/conf/context.xml  

