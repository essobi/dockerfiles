# Centos based container with Java and Tomcat  
FROM centos:centos7  
MAINTAINER V##RU  
# Install prepare infrastructure  
RUN yum -y update && \  
yum -y install wget && \  
yum -y install tar  
  
# Prepare environment  
ENV JAVA_HOME /opt/java  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin  
  
# Install Oracle Java7  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz
&& \  
tar -xvf jdk-7u79-linux-x64.tar.gz && \  
rm -rf jdk*.tar.gz && \  
mv jdk* ${JAVA_HOME}  
  
  
# Install Tomcat  
RUN wget http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.68/bin/apache-
tomcat-7.0.68.tar.gz && \  
tar -xvf apache-tomcat-7.0.68.tar.gz && \  
rm -rf apache-tomcat*.tar.gz && \  
mv apache-tomcat* ${CATALINA_HOME} && \  
sed -i '97i JAVA_OPTS="-Xms512m -Xmx1024m -XX:MaxPermSize=256m
-Dspring.profiles.active=dev,main,poll -Duser.timezone=UTC"'
${CATALINA_HOME}/bin/catalina.sh  
# Create tomcat user  
RUN groupadd -r tomcat && \  
useradd -g tomcat -d ${CATALINA_HOME} -s /sbin/nologin -c "Tomcat user" tomcat
&& \  
chown -R tomcat:tomcat ${CATALINA_HOME}  
RUN sed -i '36i <role rolename="manager-gui"/>' $CATALINA_HOME/conf/tomcat-
users.xml && \  
sed -i '37i <user username="admin" password="1234" roles="esadmin,manager-
gui"/>' $CATALINA_HOME/conf/tomcat-users.xml && \  
sed -i -e 's/52428800/152428800/g' $CATALINA_HOME/webapps/manager/WEB-
INF/web.xml  
  
WORKDIR /opt/tomcat  
#RUN rm -rf /opt/tomcat/webapps/*  
RUN rm -rf /opt/tomcat/webapps/docs && rm -rf /opt/tomcat/webapps/examples &&
rm -rf /opt/tomcat/webapps/ROOT  
  
#ADD ISMaintenance.war $CATALINA_HOME/webapps/ISMaintenance.war  
# Install Mongos  
#RUN cd / && \  
# wget http://downloads.mongodb.org/linux/mongodb-
linux-x86_64-rhel70-3.0.4.tgz && \  
# tar -xvf mongodb-linux-x86_64-rhel70-3.0.4.tgz && \  
# rm -rf mongodb-linux-x86_64-rhel70-3.0.4.tgz && \  
# mv mongodb-linux-x86_64-rhel70-3.0.4/bin/* /usr/bin/ && \  
# cd / && \  
# rm -rf mongodb-linux-x86_64-rhel70-3.0.4 && \  
# yum install mysql mailx -y  
RUN yum install mysql mailx -y && \  
cd /usr/local/bin && \  
mkdir ffmpeg && \  
cd ffmpeg && \  
wget http://ffmpeg.gusari.org/static/64bit/ffmpeg.static.64bit.latest.tar.gz
&& \  
tar zxf ffmpeg.static.64bit.latest.tar.gz && \  
mv ffmpeg /usr/bin/ && \  
mv ffprobe /usr/bin/ && \  
rm -rf /usr/local/bin/ffmpeg/ffmpeg.static.64bit.latest.tar.gz  
  
#ADD mykey /opt/mongodb/mykey  
#ADD mongod.conf /etc/mongod.conf  
#RUN chmod 600 /opt/mongodb/mykey  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
ADD redis-cli /usr/bin/redis-cli  
ADD ROOT.war /opt/tomcat/webapps/ROOT.war  
  
#mongodb ports  
#EXPOSE 27017  
#EXPOSE 27018  
#EXPOSE 27019  
#EXPOSE 30000  
#EXPOSE 30001  
#EXPOSE 30002  
#EXPOSE 30003  
#EXPOSE 30004  
#EXPOSE 30005  
#tomcat ports  
EXPOSE 8080  
EXPOSE 8089  
#redis port  
#EXPOSE 6379  
#mysql  
#EXPOSE 3306  
#rabbitmq  
#EXPOSE 5672  
#mail  
#EXPOSE 25 587 465 110 995  
ENTRYPOINT ["/run.sh"]  
  

