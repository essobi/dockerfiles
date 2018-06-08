FROM busybox  
  
MAINTAINER minanon  
  
ENV GITBUCKET_VERSION 3.0  
ADD
https://github.com/takezoe/gitbucket/releases/download/$GITBUCKET_VERSION/gitbucket.war
/tmp/gitbucket.war  
RUN mkdir -p /usr/local/tomcat/webapps/gitbucket \  
&& unzip /tmp/gitbucket.war -d /usr/local/tomcat/webapps/gitbucket \  
&& rm -f /tmp/gitbucket.war  
  
ADD files/web.xml /usr/local/tomcat/webapps/gitbucket/WEB-INF/web.xml  
  
VOLUME ["/opt/gitbucket"]  
VOLUME ["/usr/local/tomcat/webapps/gitbucket"]  

