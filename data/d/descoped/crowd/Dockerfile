FROM descoped/atlassian-base  
MAINTAINER Ove Ranheim <oranheim@gmail.com>  
  
# Install Crowd  
ENV CROWD_VERSION 3.1.2  
ENV CROWD_INST /opt/crowd  
ENV CROWD_HOME /var/atlassian-home  
  
ENV UID crowd  
ENV GID atlassian  
  
ENV CROWD_CONTEXT crowd  
ENV CROWDID_CONTEXT openidserver  
ENV OPENID_CLIENT_CONTEXT openidclient  
ENV DEMO_CONTEXT demo  
ENV SPLASH_CONTEXT ROOT  
  
ENV CROWD_URL http://localhost:8095/$CROWD_CONTEXT  
ENV LOGIN_BASE_URL http://localhost:8095  
ADD configure.bash /configure  
RUN chmod +x /configure  
  
RUN curl -Lk
http://www.atlassian.com/software/crowd/downloads/binary/atlassian-
crowd-$CROWD_VERSION.tar.gz -o /root/crowd.tar.gz \  
&& useradd -r --create-home --home-dir $CROWD_INST \--groups $GID \--shell
/bin/bash $UID \  
&& tar zxf /root/crowd.tar.gz --strip=1 -C $CROWD_INST \  
&& rm /root/crowd.tar.gz \  
&& echo "crowd.home=$CROWD_HOME" > $CROWD_INST/crowd-webapp/WEB-
INF/classes/crowd-init.properties \  
&& mv $CROWD_INST/apache-tomcat/webapps/ROOT $CROWD_INST/splash-webapp \  
&& mv $CROWD_INST/apache-tomcat/conf/Catalina/localhost $CROWD_INST/webapps \  
&& mkdir -p $CROWD_INST/apache-tomcat/conf/Catalina/localhost \  
&& touch $CROWD_INST/.crowd-is-not-configured  
  
ADD splash-context.xml $CROWD_INST/webapps/splash.xml  
  
# Launching Crowd  
WORKDIR $CROWD_INST  
VOLUME $CROWD_HOME  
  
COPY entrypoint.bash /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 8095  
CMD ["apache-tomcat/bin/catalina.sh", "run"]  

