FROM hazelcast/hazelcast:latest  
# Add your custom hazelcast.xml  
ADD hazelcast.xml $HZ_HOME  
# Run hazelcast  
CMD java -cp $HZ_HOME/hazelcast-$HZ_VERSION.jar
com.hazelcast.core.server.StartServer

