FROM lloydcotten/debian-tomcat:8-jre8  
  
ENV ERDDAP_VERSION 1.68  
ENV ERDDAP_CONTENT_URL
http://coastwatch.pfeg.noaa.gov/erddap/download/erddapContent.zip  
ENV ERDDAP_WAR_URL http://coastwatch.pfeg.noaa.gov/erddap/download/erddap.war  
  
RUN curl -fSL "$ERDDAP_CONTENT_URL" -o erddapContent.zip && \  
unzip erddapContent.zip -d $CATALINA_HOME && \  
rm erddapContent.zip  
  
RUN curl -fSL "$ERDDAP_WAR_URL" -o /root/erddap.war && \  
mv /root/erddap.war $CATALINA_HOME/webapps/  
  
COPY files/javaopts.sh $CATALINA_HOME/bin/javaopts.sh  
COPY files/setup.xml $CATALINA_HOME/content/erddap/setup.xml  
  
ENV ERDDAP_SCRATCH /erddap  
ENV DATASET_SRC /data  
RUN mkdir -p $ERDDAP_SCRATCH $DATASET_SRC  
  
EXPOSE 8080 8443  
CMD ["catalina.sh", "run"]  

