FROM hrafique/openjdk-quantal  
  
MAINTAINER Haroon Rafique https://github.com/hrafique  
  
RUN apt-get -y install wget  
RUN wget --no-verbose -O /tmp/apache-maven-3.0.5.tar.gz \  
http://archive.apache.org/dist/maven/maven-3/3.0.5/binaries/apache-
maven-3.0.5-bin.tar.gz  
# stop building if md5sum does not match  
RUN echo "94c51f0dd139b4b8549204d0605a5859 /tmp/apache-maven-3.0.5.tar.gz" | \  
md5sum -c  
  
# install in /opt/maven  
RUN mkdir -p /opt/maven  
RUN tar xzf /tmp/apache-maven-3.0.5.tar.gz --strip-components=1 \  
-C /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.0.5.tar.gz  
  
ENV MAVEN_OPTS -XX:MaxPermSize=350m -Xmx2g  
  
RUN apt-get -y install subversion  
  
# tomcat  
ENV TOMCAT_VERSION 6.0.37  
RUN mkdir -p /usr/share/tomcat  
RUN wget --no-verbose -O /tmp/apache-tomcat-$TOMCAT_VERSION.tar.gz \  
http://archive.apache.org/dist/tomcat/tomcat-6/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
# stop building if md5sum does not match  
RUN echo "f90b100cf51ae0a444bef5acd7b6edb2 /tmp/apache-
tomcat-$TOMCAT_VERSION.tar.gz" | \  
md5sum -c  
  
# install tomcat in /usr/share/tomcat  
RUN tar xzf /tmp/apache-tomcat-$TOMCAT_VERSION.tar.gz --strip-components=1 -C
/usr/share/tomcat  
RUN rm -f /tmp/apache-tomcat-$TOMCAT_VERSION.tar.gz  
ENV CATALINA_HOME /usr/share/tomcat  
ENV CATALINA_OPTS -Xmx1g -XX:MaxPermSize=300m  
  
# maven settings file  
ADD files/settings.xml /root/.m2/settings.xml  
  
ENV OJDBC_VERSION 11.2.0.2  
# oracle driver  
ADD files/ojdbc6_g-$OJDBC_VERSION.jar ojdbc6_g-$OJDBC_VERSION.jar  
# install oracle driver in local maven repo  
RUN mvn install:install-file -DgroupId=com.oracle -DartifactId=ojdbc6_g \  
-Dversion=$OJDBC_VERSION -Dpackaging=jar \  
-Dfile=ojdbc6_g-$OJDBC_VERSION.jar  
  
# install maven-dependency-plugin  
RUN mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get \  
-Dartifact=org.apache.maven.plugins:maven-dependency-plugin:2.8:jar  
  
#### setup tomcat  
# copy oracle driver to tomcat lib directory  
RUN cp ojdbc6_g-$OJDBC_VERSION.jar /usr/share/tomcat/lib  
RUN rm -rf /usr/share/tomcat/webapps/*  
ADD files/server.xml /usr/share/tomcat/conf/server.xml  
  
ENV BUILD_NUMBER 640  
# ask maven to download war artifact only (by using dependency:copy goal)  
RUN mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:copy \  
-Dartifact=org.kuali.student.web:ks-with-rice-bundled:2.1.1-FR2-M1-build-$BUILD_NUMBER:war \  
-DoutputDirectory=.  
  
RUN mkdir -p /svnexport  
  
# export sources from subversion repo  
ENV SVNEXPORT_PREFIX https://svn.kuali.org/repos/student/enrollment/ks-
deployments/tags/builds/ks-deployments-2.1/2.1.1-FR2-M1/build-$BUILD_NUMBER  
  
# export ks-impex-bundled-db  
RUN svn export -q $SVNEXPORT_PREFIX/ks-dbs/ks-impex/ks-impex-bundled-db \  
/svnexport/ks-impex-bundled-db-build-$BUILD_NUMBER  
# export ks-deployment-resources  
RUN svn export -q $SVNEXPORT_PREFIX/ks-deployment-resources \  
/svnexport/ks-deployment-resources-$BUILD_NUMBER  
  
# set some default values for environment variables  
ENV ORACLE_DBA_URL jdbc:oracle:thin:@localhost:1521:XE  
ENV ORACLE_DBA_PASSWORD manager  
ENV SKIP_DB_RESET false  
  
ADD files/launch-tomcat.sh /launch-tomcat.sh  
ADD files/rice.keystore /rice.keystore  
RUN chmod +x /launch-tomcat.sh  
  
EXPOSE 8080  
CMD /launch-tomcat.sh  

