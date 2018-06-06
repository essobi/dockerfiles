#Base  
FROM ubuntu:trusty  
MAINTAINER Carlos Ortiz<carlos.ortiz@craftercms.org>  
#Set Container Envs  
ENV JAVA_VER=8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV CRAFTER_HOME=/opt/craftercms  
ENV CATALINA_HOME=/opt/craftercms/apache-tomcat  
ENV CRAFTER_CMS_DEPLOY_HOME=/opt/craftercms/deployer  
ENV TOMCAT_MAJOR=8  
ENV TOMCAT_VERSION=8.0.32  
#Configure & Install Java (also updates)  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default oracle-
java${JAVA_VER}-unlimited-jce-policy curl git ca-certificates jsvc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer  
  
#Create CrafterCMS space  
RUN mkdir -p "$CRAFTER_HOME"  
RUN mkdir -p "$CATALINA_HOME"  
RUN mkdir -p "$CRAFTER_CMS_DEPLOY_HOME"  
  
#Change dir to CRAFTER_HOME  
WORKDIR ${CATALINA_HOME}  
#Get Tomcat  
ADD
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz ./tomcat.tar.gz  
RUN tar -xvf tomcat.tar.gz  
RUN mv apache-tomcat-${TOMCAT_VERSION}/* .  
RUN rm -rf apache-tomcat-${TOMCAT_VERSION}  
RUN rm bin/*.bat && rm tomcat.tar.gz*  
RUN echo
"shared.loader=\${catalina.base}/shared/classes,\${catalina.base}/shared/lib/*.jar"
>> conf/catalina.properties  
RUN mkdir -p shared/classes  
RUN mkdir -p shared/lib  
RUN rm -rvf ${CATALINA_HOME}/webapps/*  
  
#Expose Tomcat ports  
EXPOSE 8080  
EXPOSE 8009  
#StartTomcat!!:  
CMD ["bin/catalina.sh", "run"]  

