FROM hazelcast/hazelcast:3.9  
# Add your custom hazelcast.xml  
ADD hazelcast.xml $HZ_HOME  
ADD VERSION .  
ENV JAVA_OPTS -Xmx1g  
# Run hazelcast  
CMD ./server.sh  

