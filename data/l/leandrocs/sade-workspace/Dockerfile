FROM ubuntu:14.04  
# Install Java 8  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -q -y
software-properties-common  
RUN apt-add-repository ppa:webupd8team/java -y  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install oracle-
java8-installer -y  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#instal unzip && axel && x11 serve Installation  
RUN apt-get install -q -y axel unzip xorg git wget  
  
WORKDIR /opt/jboss  
  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 9.0.2.Final  
  
ENV DOWNLOAD_URL=http://download.jboss.org/wildfly/$WILDFLY_VERSION  
  
RUN axel ${DOWNLOAD_URL}/wildfly-$WILDFLY_VERSION.tar.gz  
RUN tar -xf wildfly-$WILDFLY_VERSION.tar.gz  
RUN rm wildfly-$WILDFLY_VERSION.tar.gz  
RUN ln -s wildfly-$WILDFLY_VERSION wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
# add management user (username: admin, passwd: wildfly)  
RUN $JBOSS_HOME/bin/add-user.sh admin wildfly --silent  
  
EXPOSE 8080 9990  
ENV WILDFLY_VERSION 9.0.2  
ENV MYSQL_CONNECTOR_VERSION 5.1.38  
RUN wget "http://central.maven.org/maven2/mysql/mysql-connector-
java/${MYSQL_CONNECTOR_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.jar" -O /opt/jboss/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar  
  
# this is to fix "Deploying non-JDBC-compliant driver class"  
RUN mkdir -p META-INF/services  
RUN echo "com.mysql.jdbc.Driver" > META-INF/services/java.sql.Driver  
RUN jar uf /opt/jboss/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}-bin.jar
META-INF  
  
ADD datasource.cli /opt/jboss/datasource.cli  
RUN sed -i -e s/MYSQL-CONNECTOR-VERSION/${MYSQL_CONNECTOR_VERSION}/g
/opt/jboss/datasource.cli  
  
RUN $JBOSS_HOME/bin/jboss-cli.sh --file=/opt/jboss/datasource.cli  
  
# Fix for WFLYCTL0056: Could not rename
/opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current to
...  
RUN rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history  
  
#install netbeans  
RUN axel
http://download.netbeans.org/netbeans/8.1/final/zip/moduleclusters/netbeans-8.1-201510222201-all-
in-one.zip  
RUN unzip netbeans-8.1-201510222201-all-in-one.zip  
  
#push project SADE IFBA Eunapolis-BA  
RUN mkdir /home/NetBeansProjects  
RUN cd /home/NetBeansProjects  
RUN git clone https://github.com/IFBAEunapolis/SADE.git  
  
#CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"] && /opt/jboss/netbeans/bin/netbeans  

