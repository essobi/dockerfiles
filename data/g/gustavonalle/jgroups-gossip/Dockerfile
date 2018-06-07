FROM jboss/base-jdk:8  
ENV JGROUPS_VERSION 3.2.7.Final  
  
ENV JGROUPS_SHA1 ed33f172801ff5784172672f1ac171e4afc1207c  
  
RUN curl -o jgroups.jar
https://repo1.maven.org/maven2/org/jgroups/jgroups/$JGROUPS_VERSION/jgroups-$JGROUPS_VERSION.jar
\  
&& sha1sum jgroups.jar | grep $JGROUPS_SHA1  
  
EXPOSE 12001  
CMD
["java","-classpath","jgroups.jar","org.jgroups.stack.GossipRouter","-port","12001"]  
  

