FROM tomcat:7-jre7  
MAINTAINER Seti <sebastian.koehlmeier@kyberna.com>  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends openssh-client && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir /node && \  
mkdir /data && \  
mkdir /deploy && \  
useradd -u 1000 -m tomcat  
  
ENV CATALINA_BASE /node  
ENV DATA /data  
ENV DEPLOY /deploy  
ENV CATALINA_TMPDIR /$CATALINA_BASE/temp  
  
# INSTALL TOMCAT  
ADD run.sh /run.sh  
RUN chmod +x /*.sh && chmod o+rx ${CATALINA_HOME} -R  
  
EXPOSE 8080  
USER 1000:1000  
CMD ["/run.sh"]  

