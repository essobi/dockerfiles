FROM jetty:9-jre8  
  
ENV JETTY_WEBAPPS /var/lib/jetty/webapps  
ENV BLAZEGRAPH_NAME bigdata  
ENV BLAZEGRAPH_PF_PARAM com.bigdata.rdf.sail.webapp.ConfigParams.propertyFile  
ENV BLAZEGRAPH_WEB_PARAM jetty.overrideDescriptor  
ENV BLAZEGRAPH_RW_PATH /RWStore.properties  
ENV BLAZEGRAPH_WEBXML_PATH /web.xml  
ENV BLAZEGRAPH_VERSION 1.5.3  
ENV BLAZEGRAPH_VERSION_URL
http://sourceforge.net/projects/bigdata/files/bigdata/${BLAZEGRAPH_VERSION}/bigdata.war/download  
  
ADD RWStore.properties $BLAZEGRAPH_RW_PATH  
ADD web.xml $BLAZEGRAPH_WEBXML_PATH  
  
RUN wget -O ${JETTY_WEBAPPS}/${BLAZEGRAPH_NAME}.war $BLAZEGRAPH_VERSION_URL  
RUN echo "JAVA_OPTIONS='${JAVA_OPTIONS}
-D${BLAZEGRAPH_PF_PARAM}=${BLAZEGRAPH_RW_PATH}
-D{BLAZEGRAPH_WEB_PARAM}=${BLAZEGRAPH_WEBXML_PATH}'" >> /etc/default/jetty  
RUN chown jetty:jetty $BLAZEGRAPH_RW_PATH $BLAZEGRAPH_WEBXML_PATH  
  
CMD ["jetty.sh", "run"]  

