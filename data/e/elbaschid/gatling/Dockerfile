FROM java  
  
ADD https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-
highcharts-bundle/2.2.3/gatling-charts-highcharts-bundle-2.2.3-bundle.zip
/var/cache/gatling.zip  
  
RUN mkdir -p /var/gatling  
RUN unzip /var/cache/gatling.zip && \  
mv gatling-charts-highcharts-bundle-2.2.3/* /var/gatling/ && \  
rm -rf gatling-charts-highcharts-bundle-2.2.3  
  
WORKDIR /var/gatling  

