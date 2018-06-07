FROM elasticsearch  
  
ADD ./GUtil.groovy /usr/share/elasticsearch/config/scripts/GUtil.groovy  
ADD ./GPatchUtil.groovy
/usr/share/elasticsearch/config/scripts/GPatchUtil.groovy  
ADD ./script.policy /usr/share/elasticsearch/config/script.policy  
  
ENV ES_JAVA_OPTS="$ES_JAVA_OPTS
-Djava.security.policy=file:///usr/share/elasticsearch/config/script.policy"  

