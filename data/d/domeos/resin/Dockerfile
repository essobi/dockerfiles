FROM domeos/java:jdk7  
  
MAINTAINER domeos  
  
ENV RESIN_VERSION 4.0.45  
ENV RESIN_HOME /opt/resin  
ENV JAVA_HOME /opt/jdk  
ENV PATH=${RESIN_HOME}/bin;${PATH}  
  
WORKDIR /opt  
  
RUN curl -ssL http://caucho.com/download/resin-pro-${RESIN_VERSION}.tar.gz -o
resin.tar.gz && \  
tar -zxvf resin.tar.gz && \  
rm -rf resin.tar.gz && \  
mv resin-pro-${RESIN_VERSION} resin  
  
EXPOSE 8080  
VOLUME "/opt/resin/webapps"  
WORKDIR /opt/resin  
  
CMD ["/opt/resin/bin/resin.sh", "console"]  
  

