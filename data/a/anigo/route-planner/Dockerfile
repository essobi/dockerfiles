FROM java:8  
  
RUN \  
mkdir -p /opt/lib && \  
cd /opt/lib && \  
wget
https://bitbucket.org/anigo/route_planner_docker/downloads/optaplanner_tsp_jar.zip
&& \  
wget https://bitbucket.org/anigo/route_planner_docker/downloads/optaplanner-
tsp.jar && \  
unzip optaplanner_tsp_jar.zip && \  
mv -f optaplanner-tsp.jar optaplanner_tsp_jar/  
  
WORKDIR /opt/lib/optaplanner_tsp_jar  
  
ENV TSP_SAS_KEY=""  
ENV OSRM_URL="http://osrm-server:5000"  
  
ENTRYPOINT ["java", "-Xmx512M", "-Djava.net.preferIPv4Stack=true"]  
CMD ["-jar", "optaplanner-tsp.jar"]

