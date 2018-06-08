FROM java  
  
ENV VERSION=2.3.0  
ADD https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-
highcharts-bundle/${VERSION}/gatling-charts-highcharts-
bundle-${VERSION}-bundle.zip /var/cache/gatling.zip  
  
RUN mkdir -p /var/gatling  
RUN unzip /var/cache/gatling.zip && \  
mv gatling-charts-highcharts-bundle-${VERSION}/* /var/gatling/ && \  
rm -rf gatling-charts-highcharts-bundle-${VERSION}  
  
WORKDIR /var/gatling  
  
ADD simulations/* /var/gatling/user-files/simulations/  
  
ENTRYPOINT ["/var/gatling/bin/gatling.sh"]  
CMD ["--simulation", "roadside.gatling.simulations.BasicSimulation"]  

