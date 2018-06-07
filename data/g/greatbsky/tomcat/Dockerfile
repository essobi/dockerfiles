FROM greatbsky/openjdk:latest  
MAINTAINER architect.bian LiuBin  
LABEL name="tomcat" license="MIT" build-date="20170621"  
  
ENV VERSION 8.5.15  
ENV TOMCAT_PATH /data/env/tomcats/0  
RUN yum update -y && cd /data/softs && wget http://www-
us.apache.org/dist/tomcat/tomcat-8/v$VERSION/bin/apache-tomcat-$VERSION.tar.gz
&& tar -zxf apache-tomcat-$VERSION.tar.gz && mkdir /data/env/tomcats && mv
apache-tomcat-$VERSION $TOMCAT_PATH && rm -rf /data/softs/*  
  
COPY catalina.sh $TOMCAT_PATH/bin/catalina.sh  
COPY server.xml $TOMCAT_PATH/conf/server.xml  
COPY context.xml $TOMCAT_PATH/conf/context.xml  
  
RUN chmod +x $TOMCAT_PATH/bin/catalina.sh  
  
WORKDIR $TOMCAT_PATH  
  
CMD ["bin/catalina.sh", "run"]  

