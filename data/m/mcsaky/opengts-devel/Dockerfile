FROM ubuntu:latest  
  
MAINTAINER mcsaky <mihai.csaky@sysop-consulting.ro>  
  
# Set the debconf frontend to Noninteractive  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
ENV GTS_HOME /usr/local/gts  
ENV CATALINA_HOME /usr/local/tomcat  
ENV GTS_VERSION 2.6.5  
ENV TOMCAT_VERSION 8.5.27  
ENV JAVA_HOME /usr/local/java  
ENV ORACLE_JAVA_HOME /usr/lib/jvm/java-8-oracle/  
  
VOLUME /usr/local/gtsconfig  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
  
RUN ln -s $ORACLE_JAVA_HOME $JAVA_HOME  
  
RUN apt-get -y install ant curl unzip sudo tar mysql-server software-
properties-common python-jinja2 python-pip  
RUN pip install j2cli  
  
RUN curl -L http://downloads.sourceforge.net/project/opengts/server-
base/$GTS_VERSION/OpenGTS_$GTS_VERSION.zip -o
/usr/local/OpenGTS_$GTS_VERSION.zip && \  
unzip /usr/local/OpenGTS_$GTS_VERSION.zip -d /usr/local && \  
ln -s /usr/local/OpenGTS_$GTS_VERSION $GTS_HOME  
  
#
http://mirrors.hostingromania.ro/apache.org/tomcat/tomcat-8/v8.0.27/bin/apache-
tomcat-8.0.27.tar.gz  
RUN curl -L
http://archive.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz -o /usr/local/tomcat.tar.gz  
  
RUN tar zxf /usr/local/tomcat.tar.gz -C /usr/local && rm
/usr/local/tomcat.tar.gz && ln -s /usr/local/apache-tomcat-$TOMCAT_VERSION
$CATALINA_HOME  
  
ADD tomcat-users.xml /usr/local/apache-tomcat-$TOMCAT_VERSION/conf/  
  
#put java.mail in place  
RUN curl -L
https://github.com/javaee/javamail/releases/download/JAVAMAIL-1_6_1/javax.mail.jar
-o $ORACLE_JAVA_HOME/jre/lib/ext/javax.mail.jar  
  
# put mysql.java in place  
# https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.45.tar.gz  
RUN curl -L http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.45.tar.gz -o /usr/local/OpenGTS_$GTS_VERSION/jlib/jdbc.mysql/mysql-
connector-java-5.1.45.tar.gz && \  
tar xvf /usr/local/OpenGTS_$GTS_VERSION/jlib/jdbc.mysql/mysql-connector-
java-5.1.45.tar.gz mysql-connector-java-5.1.45/mysql-connector-
java-5.1.45-bin.jar -O >
/usr/local/OpenGTS_$GTS_VERSION/jlib/jdbc.mysql/mysql-connector-
java-5.1.45-bin.jar && \  
rm -f /usr/local/OpenGTS_$GTS_VERSION/jlib/jdbc.mysql/mysql-connector-
java-5.1.45.tar.gz  
  
RUN cp $GTS_HOME/jlib/*/*.jar $CATALINA_HOME/lib  
RUN cp $GTS_HOME/jlib/*/*.jar $JAVA_HOME/jre/lib/ext/  
  
RUN cd $GTS_HOME; sed -i 's/\\(mysql-connector-
java\\).*.jar/\1-5.1.45-bin.jar/' build.xml; \  
sed -i 's/\\(<include name="mail.jar"\/>\\)/\1\n\t<include
name="javax.mail.jar"\/>/' build.xml; \  
sed -i 's/"mail.jar"/"javax.mail.jar"/'
src/org/opengts/tools/CheckInstall.java; \  
sed -i 's/\/\/\\*\\*\/public/public/'
src/org/opengts/war/tools/BufferedHttpServletResponse.java  
  
ADD run.sh /usr/local/apache-tomcat-$TOMCAT_VERSION/bin/  
RUN chmod 755 /usr/local/apache-tomcat-$TOMCAT_VERSION/bin/run.sh  
  
RUN rm -rf /usr/local/tomcat/webapps/examples /usr/local/tomcat/webapps/docs  
EXPOSE 8080  
CMD ["/usr/local/tomcat/bin/run.sh"]  
#CMD /bin/bash  

