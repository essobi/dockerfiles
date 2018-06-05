FROM payara/micro:latest  
  
RUN mkdir -p $PAYARA_PATH/bin  
RUN mkdir -p $PAYARA_PATH/config  
RUN mkdir -p $PAYARA_PATH/lib  
  
ADD bin/start.sh $PAYARA_PATH/bin/start.sh  
ADD bin/clusterManager.sh $PAYARA_PATH/bin/clusterManager.sh  
ADD bin/memoryConfig.sh $PAYARA_PATH/bin/memoryConfig.sh  
  
ADD config/hazelcast.xml $PAYARA_PATH/config/hazelcast.xml  
ADD lib/jelastic-gc-agent.jar $PAYARA_PATH/lib/jelastic-gc-agent.jar  
  
USER root  
RUN chmod +x $PAYARA_PATH/bin/start.sh  
RUN chmod +x $PAYARA_PATH/bin/clusterManager.sh  
RUN chmod +x $PAYARA_PATH/bin/memoryConfig.sh  
  
USER payara  
ENTRYPOINT ["/bin/bash"]  
CMD ["$PAYARA_PATH/bin/start.sh"]  

