FROM tomcat:7-jre8  
MAINTAINER jason.p.pickering@gmail.com  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
RUN wget --quiet --no-check-certificate -O -
"http://ci.dhis2.org/job/dhis2-trunk/lastSuccessfulBuild/artifact/dhis-2/dhis-
web/dhis-web-portal/target/dhis.war" \  
> /usr/local/tomcat/webapps/ROOT.war  
RUN mkdir /opt/dhis2  
RUN echo "export JAVA_OPTS=\"-Xmx2048m -server \$JAVA_OPTS\"" >
/usr/local/tomcat/bin/setenv.sh  
EXPOSE 8080  

