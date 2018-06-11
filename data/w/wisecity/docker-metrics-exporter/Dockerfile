FROM dgroup/java8-gradle  
  
COPY ./ /exporter/  
WORKDIR /exporter/  
  
RUN gradle build && mv build/libs/docker-metrics-exporter.jar . && rm -rf
build  
ADD entrypoint.sh entrypoint.sh  
RUN chmod +x entrypoint.sh  
ENTRYPOINT ["./entrypoint.sh"]  

