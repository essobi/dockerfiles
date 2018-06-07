FROM tomcat:8.0  
RUN rm -r $CATALINA_HOME/webapps/docs  
RUN rm -r $CATALINA_HOME/webapps/examples  
RUN rm -r $CATALINA_HOME/webapps/manager  
RUN rm -r $CATALINA_HOME/webapps/host-manager  
RUN rm -r $CATALINA_HOME/webapps/ROOT  
  
CMD ["catalina.sh", "run"]

