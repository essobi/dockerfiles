FROM hearstat/alpine-tomcat:7.0.65  
MAINTAINER Hearst Automation Team <atat@hearst.com>  
  
LABEL version 3.10  
  
ENV version 3.10_h2-1.4.180  
ENV CATALINA_HOME /opt/tomcat  
ENV GITBUCKET_HOME /opt/gitbucket  
  
USER root  
RUN apk add --update \  
git \  
bash \  
tar \  
&& rm -rf /var/cache/apk/*  
  
USER tomcat  
# Create gitbucket home and associated folders  
RUN mkdir -p ${GITBUCKET_HOME}/plugins\  
&& chown -R tomcat:tomcat $GITBUCKET_HOME\  
&& chmod -R 775 $GITBUCKET_HOME  
  
# Pull version of gitbucket listed above  
RUN wget
https://github.com/gitbucket/gitbucket/releases/download/${version}/gitbucket.war
\  
&& mv gitbucket.war ${CATALINA_HOME}/webapps/ROOT.war\  
&& chmod 755 ${CATALINA_HOME}/webapps/ROOT.war  
  
# Expose Gitbucket home and set as working directory  
VOLUME $GITBUCKET_HOME  
VOLUME $GITBUCKET_HOME/plugins  
WORKDIR $GITBUCKET_HOME  
  
# Expose the tomcat and ssh port needed for Gitbucket  
EXPOSE 8080  
EXPOSE 29418  
CMD [ "/opt/tomcat/bin/catalina.sh", "run" ]  

