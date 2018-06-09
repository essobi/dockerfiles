FROM lzaugg/flink-jobmanager:1.1.3_akka-2.4.12-latest  
MAINTAINER l.zaugg@mypi.ch  
  
ADD conf/flink-conf.yaml $FLINK_HOME/conf/  
  
ENV FLINK_CLASS_TO_RUN org.apache.flink.runtime.taskmanager.TaskManager  
  
ENTRYPOINT [ "/opt/flink/bin/docker_flink-run.sh" ]  
# 6125: taskmanager rpc  
# 6126: taskmanager data  
EXPOSE 6125 6126  
CMD ["--configDir", "/opt/flink/conf/" ]  

