FROM ubuntu  
  
MAINTAINER mcsaky <mihai.csaky@sysop-consulting.ro>  
  
ENV GTS_HOME /usr/local/gts  
ENV CATALINA_HOME /usr/local/tomcat  
ENV GTS_VERSION 2.5.6  
ENV TOMCAT_VERSION 7.0.54  
ENV JAVA_HOME /usr/local/java  
ENV ORACLE_JAVA_HOME /usr/lib/jvm/java-6-oracle/  
  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get update && \  
apt-get install -y python-software-properties && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java6-installer  
  
RUN ln -s $ORACLE_JAVA_HOME $JAVA_HOME  
  
RUN apt-get -y install libmysql-java liblog4j1.2-java libgnumail-java ant curl
unzip sudo tar  
  
RUN curl -L http://downloads.sourceforge.net/project/opengts/server-
base/$GTS_VERSION/OpenGTS_$GTS_VERSION.zip -o
/usr/local/OpenGTS_$GTS_VERSION.zip && \  
unzip /usr/local/OpenGTS_$GTS_VERSION.zip -d /usr/local && \  
ln -s /usr/local/OpenGTS_$GTS_VERSION $GTS_HOME  
  
RUN curl -L
http://archive.apache.org/dist/tomcat/tomcat-7/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz -o /usr/local/tomcat.tar.gz  
  
RUN tar zxf /usr/local/tomcat.tar.gz -C /usr/local && rm
/usr/local/tomcat.tar.gz && ln -s /usr/local/apache-tomcat-$TOMCAT_VERSION
$CATALINA_HOME  
  
ADD tomcat-users.xml /usr/local/apache-tomcat-$TOMCAT_VERSION/conf/  
  
#put java.mail in place  
RUN curl -L
http://java.net/projects/javamail/downloads/download/javax.mail.jar -o
/usr/local/OpenGTS_$GTS_VERSION/jlib/javamail/javax.mail.jar  
  
# put mysql.java in place  
RUN curl -L http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.31.tar.gz -o /usr/local/OpenGTS_$GTS_VERSION/jlib/jdbc.mysql/mysql-
connector-java-5.1.31.tar.gz && \  
tar xvf /usr/local/OpenGTS_$GTS_VERSION/jlib/jdbc.mysql/mysql-connector-
java-5.1.31.tar.gz mysql-connector-java-5.1.31/mysql-connector-
java-5.1.31-bin.jar -O >
/usr/local/OpenGTS_$GTS_VERSION/jlib/jdbc.mysql/mysql-connector-
java-5.1.31-bin.jar && \  
rm -f /usr/local/OpenGTS_$GTS_VERSION/jlib/jdbc.mysql/mysql-connector-
java-5.1.31.tar.gz  
  
RUN cp $GTS_HOME/jlib/*/*.jar $CATALINA_HOME/lib  
RUN cp $GTS_HOME/jlib/*/*.jar $JAVA_HOME/jre/lib/ext/  
  
RUN cd $GTS_HOME; sed -i 's/\\(mysql-connector-
java\\).*.jar/\1-5.1.31-bin.jar/' build.xml; \  
sed -i 's/\\(<include name="mail.jar"\/>\\)/\1\n\t<include
name="javax.mail.jar"\/>/' build.xml; \  
sed -i 's/"mail.jar"/"javax.mail.jar"/'
src/org/opengts/tools/CheckInstall.java  
  
ADD run.sh /usr/local/apache-tomcat-$TOMCAT_VERSION/bin/  
RUN chmod 755 /usr/local/apache-tomcat-$TOMCAT_VERSION/bin/run.sh  
  
RUN rm -rf /usr/local/tomcat/webapps/examples /usr/local/tomcat/webapps/docs  
EXPOSE 8080  
CMD ["/usr/local/tomcat/bin/run.sh"]  
  

