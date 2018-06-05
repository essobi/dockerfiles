FROM centos:centos7  
RUN yum install -y wget unzip tar  
ENV JAVA_HOME /opt/jdk/jre  
ENV PATH $PATH:/opt/jdk/jre/bin  
ENV JBOSS_DEPLOY_DIR /opt/jboss/standalone/deployments  
RUN (cd /tmp && wget --progress=dot --no-check-certificate -O jdk.tar.gz
--header "Cookie: oraclelicense=a" http://download.oracle.com/otn-
pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.tar.gz && \  
tar zxf jdk.tar.gz && \  
mv jdk1.7.0_65 /opt/jdk && \  
rm /tmp/jdk.tar.gz)  
RUN wget http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-
as-7.1.1.Final.zip -O /tmp/jboss.zip && \  
unzip -d /opt /tmp/jboss.zip && \  
mv /opt/jboss-as-7.1.1.Final /opt/jboss && \  
rm /tmp/jboss.zip  
EXPOSE 8080 9990  
COPY entrypoint.sh /docker-entry.sh  
ENTRYPOINT ["/docker-entry.sh"]  
CMD [""]  

