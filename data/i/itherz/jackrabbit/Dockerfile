FROM tomcat:9  
ADD jcr-2.0.jar /usr/local/tomcat/lib/  
ADD jcrmanager.war /usr/local/tomcat/webapps/  
  
ENV JCR_VERSION 2.15.0  
RUN cd /root && wget http://apache-
mirror.rbc.ru/pub/apache/jackrabbit/$JCR_VERSION/jackrabbit-
webapp-$JCR_VERSION.war && mv jackrabbit-webapp-$JCR_VERSION.war
/usr/local/tomcat/webapps/jackrabbit.war  
  
VOLUME /usr/local/tomcat/jackrabbit  

