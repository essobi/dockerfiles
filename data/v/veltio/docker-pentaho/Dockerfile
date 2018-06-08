FROM java:7  
MAINTAINER Gleison Silva "geison.silva@gmail.com"  
ENV MAYOR_VERSION 5.4  
ENV MINOR_VERSION 5.4.0.1-130  
ENV URL
http://downloads.sourceforge.net/project/pentaho/Business%20Intelligence%20Server/$MAYOR_VERSION  
#ENV URL http://192.168.99.1  
RUN useradd -m pentaho  
RUN mkdir /opt/pentaho  
RUN chown pentaho:pentaho /opt/pentaho  
  
# Install Pentaho Business Analytics  
RUN su -c "curl -L -s $URL/biserver-ce-$MINOR_VERSION.zip \  
-o /opt/pentaho/biserver-ce.zip && \  
unzip -q /opt/pentaho/biserver-ce.zip \  
-d /opt/pentaho/ && \  
rm -f /opt/pentaho/biserver-ce.zip" pentaho  
  
# Disable first-time startup prompt  
RUN rm /opt/pentaho/biserver-ce/promptuser.sh  
  
# Disable daemon mode for Tomcat  
RUN sed -i -e 's/\\(exec ".*"\\) start/\1 run/' /opt/pentaho/biserver-
ce/tomcat/bin/startup.sh  
  
RUN wget -c -nv --no-check-certificate https://googledrive.com/host/0B4pi-
CIMz3h1YmgyYmRlVGJVUkE/vertica-jdbc-7.1.1-0.jar \  
-O /opt/pentaho/biserver-ce/tomcat/lib/vertica.jar  
RUN wget -c -nv --no-check-certificate https://googledrive.com/host/0B4pi-
CIMz3h1YmgyYmRlVGJVUkE/jaybird-full-2.1.6.jar \  
-O /opt/pentaho/biserver-ce/tomcat/lib/jaybird.jar  
  
ADD assets /assets  
  
EXPOSE 8080  
VOLUME ${PENTAHO_FOLDER}/tomcat/logs  
VOLUME ${PENTAHO_FOLDER}/pentaho-solutions/system/repository  
  
CMD ["/assets/init"]

