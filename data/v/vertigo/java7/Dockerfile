# Base Java - Liferay - MySQL - Solr Image  
FROM vertigo/docker-base:latest  
  
MAINTAINER Rubens  
  
WORKDIR /opt  
ARG LOCALJDK  
  
ADD src/downloadJDK.sh /opt/downloadJDK.sh  
RUN sh /opt/downloadJDK.sh && \  
yum localinstall /opt/jdk.rpm -y && \  
rm /opt/jdk.rpm && \  
yum clean all  
  
ENV JAVA_HOME /usr/java/jdk1.7.0_79/bin/java  
  
RUN echo "JAVA_HOME=/usr/java/jdk1.7.0_79/bin/java" >> /etc/environment  
  
# Download Liferay Portal 6.2-ce-ga4 e descompacta  
RUN wget -q -Oliferay-portal-tomcat-6.2-ce-ga4-20150416163831865.zip
http://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.2.3%20GA4/liferay-
portal-tomcat-6.2-ce-ga4-20150416163831865.zip/download && unzip -qq liferay-
portal-tomcat-6.2-ce-ga4-20150416163831865.zip && rm -f liferay-portal-
tomcat-6.2-ce-ga4-20150416163831865.zip  
  
# Liferay aumentar memoria  
RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dfile.encoding=UTF8
-Djava.net.preferIPv4Stack=true
-Dorg.apache.catalina.loader.WebappClassLoader.ENABLE_CLEAR_REFERENCES=false
-Duser.timezone=GMT -Xmx3072m -XX:MaxPermSize=256m"' > /opt/liferay-
portal-6.2-ce-ga4/tomcat-7.0.42/bin/setenv.sh  
  
# Instalaçao do Mysql  
RUN yum install -y mysql-server && /etc/init.d/mysqld start && mysql -uroot -e
"create database liferayce" && mysql -uroot -e "GRANT ALL PRIVILEGES ON
liferayce.* TO lportal@localhost IDENTIFIED BY 'vert1234'"  
  
# Configurar banco no Liferay via arquivo db_mysql.properties  
RUN /bin/echo -e '\njdbc.default.driverClassName=com.mysql.jdbc.Driver
\njdbc.default.url=jdbc:mysql://127.0.0.1/liferayce?useUnicode=true&characterEncoding=UTF-8&useFastDateParsing=false
\njdbc.default.username=lportal \njdbc.default.password=vert1234"' >
/opt/liferay-portal-6.2-ce-ga4/db_mysql.properties  
  
RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-
properties=db_mysql.properties"' >> /opt/liferay-portal-6.2-ce-
ga4/tomcat-7.0.42/bin/setenv.sh

