FROM packagepeer/tomcat7:2  
MAINTAINER Javier Jerónimo <jjeronimo@packagepeer.com>  
  
#
################################################################################
Setup  
RUN apt-get update && apt-get install -yq curl  
  
RUN apt-get install -yq unzip && \  
mkdir -p /opt/dripstat_agent-6.1.18 && cd /opt/dripstat_agent-6.1.18 && \  
wget http://dripstat.com/dl/dripstat_agent-6.1.18.zip && \  
unzip dripstat_agent-6.1.18.zip -d ${CATALINA_HOME}  
  
ADD etc/tomcat7/web.xml ${CATALINA_HOME}/conf/web.xml  
ENV CATALINA_OPTS="${CATALINA_OPTS}"  
  
#
################################################################################
Entry point  
CMD ["/pkgp-run.sh"]  
  
ADD pkgp-run.sh /pkgp-run.sh  
RUN chmod u+x /pkgp-run.sh  
  
EXPOSE 8080  
  
#
################################################################################
Entry point  
CMD ["/pkgp-run.sh"]  

