FROM openjdk:8-jre-slim  
  
MAINTAINER renwei.han <slamhan1987@hotmail.com>  
  
RUN apt-get update; apt-get install curl unzip -y  
  
RUN curl -sL 'https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-
charts-highcharts-bundle/2.3.1/gatling-charts-highcharts-
bundle-2.3.1-bundle.zip' -o gatling-2.3.1.zip \  
&& unzip gatling-2.3.1.zip \  
&& rm gatling-2.3.1.zip \  
&& mv gatling-charts-highcharts-bundle-2.3.1 gatling  
  
# set directories below to be mountable from host  
VOLUME ["/gatling/conf", "/gatling/results", "/gatling/user-files"]  
  
WORKDIR /gatling  
  
ENTRYPOINT ["bin/gatling.sh", "-s"]  

