FROM jboss/wildfly:10.1.0.Final  
MAINTAINER José Luis Zamora Sánchez joseluiszamora@jlz.gmail.com  
EXPOSE 8080 9990  
RUN /opt/jboss/wildfly/bin/add-user.sh expertojava expertojava --silent  
COPY cursos.war /opt/jboss/wildfly/standalone/deployments/  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0",
"-bmanagement","0.0.0.0"]  

