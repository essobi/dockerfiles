FROM maxird/java:7-8  
RUN export VERSION=8.5.31 && \  
export MAJOR=`echo $VERSION | cut -c1` && \  
export
URL="https://www.apache.org/dist/tomcat/tomcat-$MAJOR/v$VERSION/bin/apache-
tomcat-$VERSION.tar.gz" && \  
cd /opt && \  
wget -q $URL && \  
tar xf apache-tomcat-${VERSION}.tar.gz -C /opt/ && \  
rm apache-tomcat-${VERSION}.tar.gz && \  
ln -s apache-tomcat-${VERSION} tomcat && \  
rm -rf /opt/tomcat/webapps/*  
  
CMD ["/opt/tomcat/bin/catalina.sh", "run"]  

