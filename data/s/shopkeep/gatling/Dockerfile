FROM shopkeep/sbt:0.13.8  
ENV GATLING_VERSION 2.1.7  
WORKDIR /usr/local  
  
RUN curl -o gatling-${GATLING_VERSION}.zip
https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-
highcharts-bundle/${GATLING_VERSION}/gatling-charts-highcharts-
bundle-${GATLING_VERSION}-bundle.zip  
RUN unzip gatling-${GATLING_VERSION}.zip  
RUN rm gatling-${GATLING_VERSION}.zip  
RUN mv gatling-charts-highcharts-bundle-${GATLING_VERSION} gatling  
RUN rm -rf gatling/user-files/*  
RUN rm -rf gatling/results  
  
ENTRYPOINT ["/usr/local/gatling/bin/gatling.sh"]  

