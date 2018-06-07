####### BASE ############  
FROM jboss/wildfly:8.2.0.Final  
  
####### MAINTAINER ############  
MAINTAINER Wong Liong Hung <lhwong@gmail.com>  
  
####### ENVIRONMENT ############  
ENV JBOSS_BIND_ADDRESS 0.0.0.0  
ENV OPTAPLANNER_VERSION 6.5.0.Final  
ENV OPTAPLANNER_CONTEXT_PATH optaplanner  
  
  
  
# Fetch the optaplanner package  
RUN curl -o $HOME/optaplanner.zip \  
http://download.jboss.org/optaplanner/release/$OPTAPLANNER_VERSION/optaplanner-
distribution-$OPTAPLANNER_VERSION.zip && \  
# unzip optaplanner  
unzip $HOME/optaplanner.zip -d $HOME && \  
mv $HOME/optaplanner-
distribution-$OPTAPLANNER_VERSION/webexamples/binaries/optaplanner-
webexamples-$OPTAPLANNER_VERSION.war \  
$JBOSS_HOME/standalone/deployments/$OPTAPLANNER_CONTEXT_PATH.war && \  
touch
$JBOSS_HOME/standalone/deployments/$OPTAPLANNER_CONTEXT_PATH.war.dodeploy && \  
rm -fr $HOME/optaplanner*  
  
####### CONFIGURATION ############  
USER root  
ADD etc/start_optaplanner.sh $JBOSS_HOME/bin/start_optaplanner.sh  
RUN chown jboss:jboss $JBOSS_HOME/standalone/deployments/*  
RUN chown jboss:jboss $JBOSS_HOME/bin/start_optaplanner.sh  
RUN chmod u+x $JBOSS_HOME/bin/start_optaplanner.sh  
  
####### CUSTOM JBOSS USER ############  
# Switchback to jboss user  
USER jboss  
  
  
####### RUNNING OPTAPLANNER ############  
WORKDIR $JBOSS_HOME/bin/  
CMD ["./start_optaplanner.sh"]

