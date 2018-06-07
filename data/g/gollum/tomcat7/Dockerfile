# version: 0.0.1  
FROM gollum/jre7:latest  
  
MAINTAINER Gollum 'jianqiao.ms@foxmail.com'  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.77  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
ENV PKG tomcat.tar.gz  
ENV DIR tomcat  
ENV DST /usr/local/tomcat  
ENV PROFILE /etc/profile.d/tomcat.sh  
  
RUN yum install -y wget  
RUN mkdir $DIR  
RUN wget -O $PKG "$TOMCAT_TGZ_URL" && \  
tar zxvf $PKG \--strip-components=1 -C $DIR && rm -rf $DIR/webapps/* && \  
mv $DIR /opt/ && ln -s /opt/$DIR $DST && \  
rm -rf $PKG && \  
echo "CATALINA_HOME=$DST" > $PROFILE && \  
echo 'pathmunge $CATALINA_HOME/bin' >> $PROFILE  
  
VOLUME /usr/local/tomcat/webapps/  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

