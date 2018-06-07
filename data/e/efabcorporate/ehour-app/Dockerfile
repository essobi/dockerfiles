##############################################################  
# Crée un container docker pour l'application eHour  
##############################################################  
FROM tomcat:8.5.11-jre8-alpine  
MAINTAINER Fredice NJAKO "fredice.njako@efab-corporate.com"  
##########################################################  
  
##########################################################  
# Récupération du war  
##########################################################  
ENV EHOUR_VERSION "1.4.3"  
ENV EHOUR_HOME "/opt/ehour/ehour-$EHOUR_VERSION"  
RUN echo $EHOUR_HOME  
ENV TOMCAT_HOME "/usr/local/tomcat"  
  
RUN mkdir -p /opt/ehour  
WORKDIR /opt/ehour  
RUN wget http://ehour.nl/download/downloadfile.php?get=ehour-$EHOUR_VERSION-
war.zip -O ehour-war.zip  
RUN unzip ehour-war.zip  
RUN rm ehour-war.zip  
WORKDIR $EHOUR_HOME  
##########################################################  
##########################################################  
# Déploiement du war  
##########################################################  
RUN echo 'export EHOUR_HOME="'"$EHOUR_HOME"'"' > $TOMCAT_HOME/bin/setenv.sh  
RUN chmod 755 $TOMCAT_HOME/bin/setenv.sh  
RUN cp $EHOUR_HOME/app/*.war $TOMCAT_HOME/webapps/ehour.war  
COPY conf/ehour.properties $EHOUR_HOME/conf/  
##########################################################  
  
##########################################################  
# Lancement du conteneur  
##########################################################  
EXPOSE 8080 443  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]  
CMD ["catalina.sh", "run"]  
##########################################################

