FROM java:8-jre  
  
ENV DRILL 1.7.0  
ENV APACHE /opt/apache  
RUN mkdir -p $APACHE/archive $APACHE/drill  
  
ENV PACKAGE apache-drill-$DRILL.tar.gz  
  
RUN wget
"http://www.apache.org/dyn/closer.lua?filename=drill/drill-$DRILL/$PACKAGE&action=download"
\--output-document=$APACHE/archive/drill.tar.gz  
  
RUN tar -xzvf $APACHE/archive/drill.tar.gz --directory $APACHE/drill --strip-
components=1  
  
ENV DRILL_CONF_DIR $APACHE/drill/conf  
  
ADD conf/ $DRILL_CONF_DIR/  
  
WORKDIR $APACHE  
  
ENTRYPOINT [ "drill/bin/runbit" ]  

