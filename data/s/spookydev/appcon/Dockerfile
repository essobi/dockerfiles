FROM centos:latest  
MAINTAINER spookydev "spookydev@mailbox.org"  
ENV JAVA_VERSION_MAJOR=8  
ENV JAVA_VERSION_MINOR=144  
#ENV JAVA_VERSION_BUILD=01  
USER root  
  
RUN groupadd -r appuser -g 2817 && groupadd -r appusers -g 2542 && useradd -u
2817 -g 2817 -G appusers appuser  
RUN chown -R appuser:appuser /tmp  
RUN unlink /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Zurich
/etc/localtime  
  
RUN yum update -y && cd /opt  
  
COPY jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.rpm /opt  
RUN cd /opt && yum -y localinstall
jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.rpm && rm -f
jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.rpm && yum clean all  
#ENV JRE_HOME /usr/bin/java  
#ENV PATH $PATH:$JRE_HOME/bin  
WORKDIR /opt  
COPY apache-tomcat-8.5.20.tar.gz .  
RUN mkdir -p tomcat && tar -xf apache-tomcat-8.5.20.tar.gz -C tomcat && rm -f
apache-tomcat-8.5.20.tar.gz  
RUN ln -s /opt/tomcat/apache-tomcat-8.5.20 /opt/tomcat/current  
RUN mkdir -p tomcat/logs  
RUN chown -R appuser:appusers tomcat/apache-tomcat-8.5.20  
COPY tomcat/conf/tomcat-users.xml /opt/tomcat/current/conf  
COPY tomcat/manager/context.xml /opt/tomcat/current/webapps/manager/META-INF  
COPY tomcat/host-manager/context.xml /opt/tomcat/current/webapps/host-
manager/META-INF  
  
ENV CATALINA_HOME /opt/tomcat/apache-tomcat-8.5.20/  
  
EXPOSE 8080  
USER appuser  
CMD ["/opt/tomcat/apache-tomcat-8.5.20/bin/catalina.sh", "run"]  
  

