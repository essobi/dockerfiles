FROM hazelcast/hazelcast:3.6.2  
EXPOSE 5701-5800  
# Add your custom hazelcast.xml  
ADD hazelcast.xml $HZ_HOME  
# Run hazelcast  
CMD java -DHZ_GROUP_NAME=$HZ_GROUP_NAME -DHZ_GROUP_PASSWORD=$HZ_GROUP_PASSWORD
-cp $HZ_HOME/hazelcast-all-$HZ_VERSION.jar
com.hazelcast.core.server.StartServer

