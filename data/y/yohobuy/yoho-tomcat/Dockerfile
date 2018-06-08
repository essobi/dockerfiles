############################################################  
# Dockerfile to build centos 6.7 \+ java + tomcat  
# Based on centos 6.7  
# How to build new image: docker build -t yoho-tomcat  
  
############################################################  
  
#base image  
FROM yohobuy/yoho-java:latest  
  
MAINTAINER chunhua.zhang <chunhua.zhang@yoho.cn>  
  
#tomcat env  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
# install tomcat  
ENV TOMCAT_VERSION 8.5.16  
  
RUN wget http://blob.yohops.com/software/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz && \  
rm apache-tomcat*.tar.gz && \  
mv apache-tomcat* ${CATALINA_HOME} && \  
rm -rf ${CATALINA_HOME}/webapps/*  
  
  
RUN chmod +x ${CATALINA_HOME}/bin/*sh  
  
  
WORKDIR $CATALINA_HOME  
  
#expose port: 8080  
EXPOSE 8080  
  
#running cmd  
CMD ["catalina.sh", "run"]  

