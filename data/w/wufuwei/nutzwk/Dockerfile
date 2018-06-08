FROM keensoft/centos7-java8  
  
MAINTAINER wufuwei "oradb@163.com"  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.4  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN yum -y install unzip  
  
RUN cd $CATALINA_HOME \  
&&wget -O tomcat.tar.gz $TOMCAT_TGZ_URL \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& cd $CATALINA_HOME \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
&& rm -fr /usr/local/tomcat/webapps/* \  
  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_MAJOR 3  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_TGZ_URL
http://mirrors.cnnic.cn/apache/maven/maven-$MAVEN_MAJOR/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz  
ENV NUTZWK_TAG_NAME=bootstrap  
ENV NUTZWK_TGZ_URL
https://github.com/wufuwei/NutzWk/archive/$NUTZWK_TAG_NAME.zip  
  
  
RUN mkdir /tmp2 && cd /tmp2 \  
&& wget -O maven.tar.gz $MAVEN_TGZ_URL && tar xzf maven.tar.gz -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& wget -O Nutzwk.zip $NUTZWK_TGZ_URL \  
&& unzip -d /tmp2 Nutzwk.zip \  
&& cd /tmp2 && cd NutzWk-$NUTZWK_TAG_NAME \  
&& mvn clean package \  
&& cp -r target/nutzwk.war /usr/local/tomcat/webapps/ROOT.war \  
&& cd / \  
&& rm -fr /tmp2 usr/share/maven /usr/bin/mvn ~/.m2  
  
WORKDIR $CATALINA_HOME  
  
EXPOSE 8080  
COPY docker-entrypoint.py /entrypoint.py  
CMD ["python", "/entrypoint.py"]  
ENV LANG C.UTF-8  
ENV TZ "Asia/Shanghai"  
ENV "ehcache.disk.store.dir" "/data"  
VOLUME /data  
  
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]  
  

