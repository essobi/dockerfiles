FROM domeos/java:jdk7  
  
MAINTAINER domeos  
  
ENV JETTY_VERSION 8.1.17.v20150415  
ENV JETTY_HOME /opt/jetty  
ENV JAVA_HOME /opt/jdk  
ENV PATH=${JETTY_HOME}/bin:${PATH}  
  
WORKDIR /opt  
  
RUN curl -ssL http://download.eclipse.org/jetty/${JETTY_VERSION}/dist/jetty-
distribution-${JETTY_VERSION}.tar.gz -o jetty.tar.gz && \  
tar -zxvf jetty.tar.gz -C /opt/ && \  
rm -rf jetty.tar.gz && \  
mv /opt/jetty-distribution-* /opt/jetty  
  
EXPOSE 8080  
VOLUME ["/opt/jetty/"]  
WORKDIR /opt/jetty  
  
CMD ["java", "-jar", "start.jar"]  
  

