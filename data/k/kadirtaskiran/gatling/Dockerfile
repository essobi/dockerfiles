FROM kadirtaskiran/jetty:base_java8  
  
ENV GATLING_VERSION 2.1.6  
RUN apt-get install unzip -y  
  
# Install Gatling  
RUN curl -L -v http://repo1.maven.org/maven2/io/gatling/highcharts/gatling-
charts-highcharts-bundle/${GATLING_VERSION}/gatling-charts-highcharts-
bundle-${GATLING_VERSION}-bundle.zip -o gatling-charts-
highcharts-${GATLING_VERSION}-bundle.zip  
RUN unzip gatling-charts-highcharts-${GATLING_VERSION}-bundle.zip  
RUN rm -f gatling-charts-highcharts-${GATLING_VERSION}-bundle.zip  
RUN mv gatling-charts-highcharts-${GATLING_VERSION} /opt/gatling  
  
VOLUME /opt/gatling/conf  
VOLUME /opt/gatling/results  
VOLUME /opt/gatling/user-files  
  
ENV PATH $PATH:/opt/gatling/bin  
ENV GATLING_HOME /opt/gatling  
  
ENTRYPOINT ["gatling.sh"]  

